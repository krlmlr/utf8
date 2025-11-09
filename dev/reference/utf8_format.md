# UTF-8 Text Formatting

Format a character object for UTF-8 printing.

## Usage

``` r
utf8_format(
  x,
  ...,
  trim = FALSE,
  chars = NULL,
  justify = "left",
  width = NULL,
  na.encode = TRUE,
  quote = FALSE,
  na.print = NULL,
  print.gap = NULL,
  utf8 = NULL
)
```

## Arguments

- x:

  character object.

- ...:

  These dots are for future extensions and must be empty.

- trim:

  logical scalar indicating whether to suppress padding spaces around
  elements.

- chars:

  integer scalar indicating the maximum number of character units to
  display. Wide characters like emoji take two character units;
  combining marks and default ignorables take none. Longer strings get
  truncated and suffixed or prefixed with an ellipsis (`"..."` or
  `"\u2026"`, whichever is most appropriate for the current character
  locale). Set to `NULL` to limit output to the line width as determined
  by `getOption("width")`.

- justify:

  justification; one of `"left"`, `"right"`, `"centre"`, or `"none"`.
  Can be abbreviated.

- width:

  the minimum field width; set to `NULL` or `0` for no restriction.

- na.encode:

  logical scalar indicating whether to encode `NA` values as character
  strings.

- quote:

  logical scalar indicating whether to format for a context with
  surrounding double-quotes (`'"'`) and escaped internal double-quotes.

- na.print:

  character string (or `NULL`) indicating the encoding for `NA` values.
  Ignored when `na.encode` is `FALSE`.

- print.gap:

  non-negative integer (or `NULL`) giving the number of spaces in gaps
  between columns; set to `NULL` or `1` for a single space.

- utf8:

  logical scalar indicating whether to format for a UTF-8 capable
  display (ASCII-only otherwise), or `NULL` to format for output
  capabilities as determined by
  [`output_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/output_utf8.md).

## Value

A character object with the same attributes as `x` but with `Encoding`
set to `"UTF-8"` for elements that can be converted to valid UTF-8 and
`"bytes"` for others.

## Details

`utf8_format()` formats a character object for printing, optionally
truncating long character strings.

## See also

[`utf8_print()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_print.md),
[`utf8_encode()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_encode.md).

## Examples

``` r
# the second element is encoded in latin-1, but declared as UTF-8
x <- c("fa\u00E7ile", "fa\xE7ile", "fa\xC3\xA7ile")
Encoding(x) <- c("UTF-8", "UTF-8", "bytes")

# formatting
utf8_format(x, chars = 3)
#> [1] "faç…"  "fa..." "fa..."
utf8_format(x, chars = 3, justify = "centre", width = 10)
#> [1] "   faç…   " "  fa...   " "  fa...   "
utf8_format(x, chars = 3, justify = "right")
#> [1] "…ile"       "...\\xe7ile" "...\\xa7ile"
```
