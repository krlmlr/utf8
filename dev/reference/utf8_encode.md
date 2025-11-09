# Encode Character Object as for UTF-8 Printing

Escape the strings in a character object, optionally adding quotes or
spaces, adjusting the width for display.

## Usage

``` r
utf8_encode(
  x,
  ...,
  width = 0L,
  quote = FALSE,
  justify = "left",
  escapes = NULL,
  display = FALSE,
  utf8 = NULL
)
```

## Arguments

- x:

  character object.

- ...:

  These dots are for future extensions and must be empty.

- width:

  integer giving the minimum field width; specify `NULL` or `NA` for no
  minimum.

- quote:

  logical scalar indicating whether to surround results with
  double-quotes and escape internal double-quotes.

- justify:

  justification; one of `"left"`, `"right"`, `"centre"`, or `"none"`.
  Can be abbreviated.

- escapes:

  a character string specifying the display style for the backslash
  escapes, as an ANSI SGR parameter string, or NULL for no styling.

- display:

  logical scalar indicating whether to optimize the encoding for
  display, not byte-for-byte data transmission.

- utf8:

  logical scalar indicating whether to encode for a UTF-8 capable
  display (ASCII-only otherwise), or `NULL` to encode for output
  capabilities as determined by
  [`output_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/output_utf8.md).

## Value

A character object with the same attributes as `x` but with `Encoding`
set to `"UTF-8"`.

## Details

`utf8_encode()` encodes a character object for printing on a UTF-8
device by escaping controls characters and other non-printable
characters. When `display = TRUE`, the function optimizes the encoding
for display by removing default ignorable characters (soft hyphens,
zero-width spaces, etc.) and placing zero-width spaces after wide emoji.
When
[`output_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/output_utf8.md)
is `FALSE` the function escapes all non-ASCII characters and gives the
same results on all platforms.

## See also

[`utf8_print()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_print.md).

## Examples

``` r
# the second element is encoded in latin-1, but declared as UTF-8
x <- c("fa\u00E7ile", "fa\xE7ile", "fa\xC3\xA7ile")
Encoding(x) <- c("UTF-8", "UTF-8", "bytes")

# encoding
utf8_encode(x)
#> [1] "façile"          "fa\\xe7ile"      "fa\\xc3\\xa7ile"

# add style to the escapes
cat(utf8_encode("hello\nstyled\\world", escapes = "1"), "\n")
#> hello\nstyled\\world 
```
