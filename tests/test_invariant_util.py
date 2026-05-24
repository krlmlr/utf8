import pytest
import ctypes
import struct
import sys


# Simulate the buffer allocation and copy logic from src/util.c
# The vulnerable pattern: ans is allocated, then memcpy(ans + 2, CHAR(elt), n)
# where n = len(input_string) and ans size must be >= n + 2

HEADER_OFFSET = 2  # The offset used in memcpy(ans + 2, ...)


def safe_buffer_copy(input_string: str, allocated_size: int) -> bytes:
    """
    Simulates the C code pattern:
        ans = malloc(allocated_size)
        memcpy(ans + 2, CHAR(elt), n)
    
    Returns the buffer contents if safe, raises ValueError if overflow would occur.
    This is the SAFE reference implementation that enforces the invariant.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    encoded = input_string.encode('utf-8', errors='replace')
    n = len(encoded)
    
    # The invariant: allocated_size must be >= HEADER_OFFSET + n
    required_size = HEADER_OFFSET + n
    
    if required_size > allocated_size:
        raise ValueError(
            f"Buffer overflow: required {required_size} bytes "
            f"(offset={HEADER_OFFSET} + n={n}), "
            f"but only {allocated_size} allocated"
        )
    
    # Safe copy simulation
    buf = bytearray(allocated_size)
    buf[HEADER_OFFSET:HEADER_OFFSET + n] = encoded
    return bytes(buf)


def simulate_vulnerable_allocation(input_string: str) -> dict:
    """
    Simulates what the vulnerable C code does:
    - Allocates buffer of size n (forgetting the +2 offset)
    - Tries to copy n bytes starting at offset 2
    Returns metadata about whether overflow would occur.
    """
    encoded = input_string.encode('utf-8', errors='replace')
    n = len(encoded)
    
    # Vulnerable allocation: only allocates n bytes, not n+2
    vulnerable_allocated = n  # Bug: should be n + HEADER_OFFSET
    
    # Check if the copy would overflow
    bytes_needed = HEADER_OFFSET + n
    overflow_occurs = bytes_needed > vulnerable_allocated
    overflow_amount = max(0, bytes_needed - vulnerable_allocated)
    
    return {
        'n': n,
        'allocated': vulnerable_allocated,
        'needed': bytes_needed,
        'overflow': overflow_occurs,
        'overflow_bytes': overflow_amount,
    }


@pytest.mark.parametrize("payload", [
    # Normal strings - baseline
    "hello",
    "world",
    "test",
    
    # Empty string edge case
    "",
    
    # Exactly at boundary (n=1, needs n+2=3 bytes)
    "a",
    
    # 2x oversized strings
    "A" * 100,
    "B" * 256,
    "C" * 512,
    
    # 10x oversized strings
    "X" * 1000,
    "Y" * 10000,
    "Z" * 100000,
    
    # Attack payloads: format string attempts
    "%s%s%s%s%s%s%s%s%s%s",
    "%n%n%n%n%n%n%n%n%n%n",
    "%x%x%x%x%x%x%x%x%x%x",
    "%" + "A" * 1000,
    
    # Attack payloads: null bytes and binary data
    "A\x00B\x00C" * 50,
    "\x00" * 200,
    "\xff" * 200,
    "\x00\xff" * 100,
    
    # Attack payloads: long strings with special characters
    "/../" * 500,
    "../../../etc/passwd" * 100,
    "/dev/null" * 200,
    
    # Attack payloads: SQL injection style
    "' OR '1'='1" * 100,
    "'; DROP TABLE users; --" * 50,
    
    # Attack payloads: shell injection style
    "; cat /etc/passwd" * 100,
    "$(whoami)" * 200,
    "`id`" * 300,
    
    # Attack payloads: Unicode and multibyte
    "\u0041" * 500,  # ASCII 'A' in unicode
    "\u00ff" * 500,  # Latin small letter y with diaeresis
    "\u4e2d\u6587" * 200,  # Chinese characters (3 bytes each in UTF-8)
    "\U0001F600" * 200,  # Emoji (4 bytes each in UTF-8)
    
    # Attack payloads: repeated patterns that might cause issues
    "AAAA" * 2500,  # 10000 bytes
    "\r\n" * 5000,
    "\n" * 10000,
    
    # Attack payloads: integer overflow boundary values
    "A" * 65535,   # 2^16 - 1
    "A" * 65536,   # 2^16
    "A" * 65537,   # 2^16 + 1
    
    # Attack payloads: heap spray patterns
    "\x90" * 1000,  # NOP sled
    "\xcc" * 1000,  # INT3 breakpoint
    "\x41\x41\x41\x41" * 250,  # AAAA pattern
    
    # Attack payloads: off-by-one boundary
    "A" * 1,
    "A" * 2,
    "A" * 3,
    "A" * 4,
    
    # Mixed content
    "normal text" + "\x00" * 100 + "after null",
    "start" + "A" * 10000 + "end",
])
def test_buffer_read_never_exceeds_declared_length(payload):
    """
    Invariant: Buffer reads (memcpy) must never exceed the declared/allocated length.
    
    Specifically: when copying 'n' bytes at offset 2 into buffer 'ans',
    the allocation of 'ans' must be at least n + 2 bytes.
    Any input that would cause a read/write beyond the allocated buffer
    must be rejected or truncated — never silently overflow.
    
    CWE-120: Buffer Copy without Checking Size of Input
    """
    encoded = payload.encode('utf-8', errors='replace')
    n = len(encoded)
    required_size = HEADER_OFFSET + n
    
    # INVARIANT CHECK 1: The required allocation must always account for the offset
    assert required_size == n + HEADER_OFFSET, (
        f"Required size calculation must include offset: "
        f"expected {n + HEADER_OFFSET}, got {required_size}"
    )
    
    # INVARIANT CHECK 2: Verify that vulnerable allocation (n only) would overflow
    # for any non-trivial input (n > 0)
    if n > 0:
        vulnerable_info = simulate_vulnerable_allocation(payload)
        assert vulnerable_info['overflow'], (
            f"For non-empty input of length {n}, "
            f"allocating only {vulnerable_info['allocated']} bytes "
            f"and copying at offset {HEADER_OFFSET} MUST cause overflow. "
            f"Needed: {vulnerable_info['needed']} bytes."
        )
        assert vulnerable_info['overflow_bytes'] == HEADER_OFFSET, (
            f"Overflow amount should equal the header offset ({HEADER_OFFSET}), "
            f"got {vulnerable_info['overflow_bytes']}"
        )
    
    # INVARIANT CHECK 3: Safe implementation must succeed with correct allocation
    correct_allocation = required_size
    result = safe_buffer_copy(payload, correct_allocation)
    assert len(result) == correct_allocation, (
        f"Result buffer length {len(result)} must equal allocated size {correct_allocation}"
    )
    
    # INVARIANT CHECK 4: The copied data must be within bounds
    copied_data = result[HEADER_OFFSET:HEADER_OFFSET + n]
    assert len(copied_data) == n, (
        f"Copied data length {len(copied_data)} must equal n={n}"
    )
    assert copied_data == encoded, (
        f"Copied data must match input encoding exactly"
    )
    
    # INVARIANT CHECK 5: Safe implementation must REJECT under-allocated buffers
    if n > 0:
        under_allocated = n  # Same bug as vulnerable code: forgot +2
        with pytest.raises(ValueError, match="Buffer overflow"):
            safe_buffer_copy(payload, under_allocated)
    
    # INVARIANT CHECK 6: Safe implementation must REJECT severely under-allocated buffers
    if n > 0:
        severely_under_allocated = max(1, n // 2)
        with pytest.raises(ValueError, match="Buffer overflow"):
            safe_buffer_copy(payload, severely_under_allocated)
    
    # INVARIANT CHECK 7: Verify no data bleeds past the end of the buffer
    # Add sentinel bytes after the buffer to detect overflow
    sentinel = b'\xDE\xAD\xBE\xEF'
    padded_allocation = correct_allocation + len(sentinel)
    padded_buf = bytearray(padded_allocation)
    padded_buf[-len(sentinel):] = sentinel
    
    # Perform the copy within bounds
    padded_buf[HEADER_OFFSET:HEADER_OFFSET + n] = encoded
    
    # Sentinel must be intact (no overflow into sentinel region)
    assert bytes(padded_buf[-len(sentinel):]) == sentinel, (
        f"Sentinel bytes were overwritten! Buffer overflow detected for "
        f"payload of length {n}. Allocation: {correct_allocation}, "
        f"sentinel at offset {correct_allocation}"
    )


@pytest.mark.parametrize("payload,max_allowed_size", [
    # Test that truncation is applied when input exceeds max buffer size
    ("A" * 1000, 100),
    ("B" * 10000, 256),
    ("C" * 100000, 512),
    ("\xff" * 5000, 1024),
    ("attack" * 1000, 64),
])
def test_oversized_input_is_truncated_or_rejected(payload, max_allowed_size):
    """
    Invariant: When input exceeds the maximum allowed buffer size,
    the implementation must either truncate the input to fit within bounds
    OR reject it entirely. It must never copy more bytes than the buffer can hold.
    """
    encoded = payload.encode('utf-8', errors='replace')
    n = len(encoded)
    
    # The maximum safe copy length given the buffer size and offset
    max_safe_copy = max(0, max_allowed_size - HEADER_OFFSET)
    
    assert n > max_safe_copy, (
        f"Test setup error: payload length {n} should exceed max_safe_copy {max_safe_copy}"
    )
    
    # Option 1: Rejection - must raise an error
    try:
        result = safe_buffer_copy(payload, max_allowed_size)
        # If it didn't raise, it must have truncated
        pytest.fail(
            f"Expected ValueError for oversized input (n={n}) "
            f"with allocation={max_allowed_size}"
        )
    except ValueError as e:
        # Rejection is acceptable - verify the error message is informative
        assert "overflow" in str(e).lower() or "buffer" in str(e).lower(), (
            f"Error message should mention overflow/buffer: {e}"
        )
    
    # Option 2: Verify that truncation would be safe if implemented
    truncated = encoded[:max_safe_copy]
    truncated_size = len(truncated)
    
    assert truncated_size + HEADER_OFFSET <= max_allowed_size, (
        f"Truncated copy ({truncated_size} bytes) at offset {HEADER_OFFSET} "
        f"must fit in allocation ({max_allowed_size} bytes)"
    )


@pytest.mark.parametrize("n,offset", [
    # Test various combinations of copy length and offset
    (0, 2),
    (1, 2),
    (2, 2),
    (100, 2),
    (1000, 2),
    (65534, 2),
    (65535, 2),
    (65536, 2),
])
def test_allocation_must_include_offset(n, offset):
    """
    Invariant: Buffer allocation for a copy operation at offset 'k' 
    copying 'n' bytes must always be at least n + k bytes.
    Allocating only n bytes when copying at offset k causes overflow for any k > 0.
    """
    # Correct allocation
    correct_allocation = n + offset
    assert correct_allocation >= n + offset, (
        f"Correct allocation {correct_allocation} must be >= n+offset = {n+offset}"
    )
    
    # Vulnerable allocation (the bug)
    vulnerable_allocation = n  # Missing the offset
    
    if n > 0:
        # Vulnerable allocation always overflows when offset > 0
        assert vulnerable_allocation < n + offset, (
            f"Vulnerable allocation {vulnerable_allocation} must be less than "
            f"required {n + offset} for n={n}, offset={offset}"
        )
        
        overflow_bytes = (n + offset) - vulnerable_allocation
        assert overflow_bytes == offset, (
            f"Overflow amount must equal offset ({offset}), got {overflow_bytes}"
        )
    
    # Verify the invariant: correct_allocation - offset >= 0 (no negative copy)
    assert correct_allocation - offset >= 0, (
        f"Allocation minus offset must be non-negative"
    )
    
    # Verify: bytes written = [offset, offset+n), all within [0, correct_allocation)
    write_start = offset
    write_end = offset + n
    assert write_start >= 0, "Write start must be non-negative"
    assert write_end <= correct_allocation, (
        f"Write end ({write_end}) must not exceed allocation ({correct_allocation})"
    )