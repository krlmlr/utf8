# Measure the Character String Width

Compute the display widths of the elements of a character object.

## Usage

``` r
utf8_width(x, ..., encode = TRUE, quote = FALSE, utf8 = NULL)
```

## Arguments

- x:

  character object.

- ...:

  These dots are for future extensions and must be empty.

- encode:

  whether to encode the object before measuring its width.

- quote:

  whether to quote the object before measuring its width.

- utf8:

  logical scalar indicating whether to determine widths assuming a UTF-8
  capable display (ASCII-only otherwise), or `NULL` to format for output
  capabilities as determined by
  [`output_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/output_utf8.md).

## Value

An integer object, with the same `names`, `dim`, and `dimnames` as `x`.

## Details

`utf8_width()` returns the printed widths of the elements of a character
object on a UTF-8 device (or on an ASCII device when
[`output_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/output_utf8.md)
is `FALSE`), when printed with
[`utf8_print()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_print.md).
If the string is not printable on the device, for example if it contains
a control code like `"\n"`, then the result is `NA`. If `encode = TRUE`,
the default, then the function returns the widths of the encoded
elements via
[`utf8_encode()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_encode.md));
otherwise, the function returns the widths of the original elements.

## See also

[`utf8_print()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_print.md).

## Examples

``` r
# the second element is encoded in latin-1, but declared as UTF-8
x <- c("fa\u00E7ile", "fa\xE7ile", "fa\xC3\xA7ile")
Encoding(x) <- c("UTF-8", "UTF-8", "bytes")

# get widths
utf8_width(x)
#> [1]  6  9 13
utf8_width(x, encode = FALSE)
#> [1]  6 NA NA
utf8_width('"')
#> [1] 1
utf8_width('"', quote = TRUE)
#> [1] 4
```
