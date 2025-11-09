# Print UTF-8 Text

Print a UTF-8 character object.

## Usage

``` r
utf8_print(
  x,
  ...,
  chars = NULL,
  quote = TRUE,
  na.print = NULL,
  print.gap = NULL,
  right = FALSE,
  max = NULL,
  names = NULL,
  rownames = NULL,
  escapes = NULL,
  display = TRUE,
  style = TRUE,
  utf8 = NULL
)
```

## Arguments

- x:

  character object.

- ...:

  These dots are for future extensions and must be empty.

- chars:

  integer scalar indicating the maximum number of character units to
  display. Wide characters like emoji take two character units;
  combining marks and default ignorables take none. Longer strings get
  truncated and suffixed or prefixed with an ellipsis (`"..."` in C
  locale, `"\u2026"` in others). Set to `NULL` to limit output to the
  line width as determined by `getOption("width")`.

- quote:

  logical scalar indicating whether to put surrounding double-quotes
  (`'"'`) around character strings and escape internal double-quotes.

- na.print:

  character string (or `NULL`) indicating the encoding for `NA` values.
  Ignored when `na.encode` is `FALSE`.

- print.gap:

  non-negative integer (or `NULL`) giving the number of spaces in gaps
  between columns; set to `NULL` or `1` for a single space.

- right:

  logical scalar indicating whether to right-justify character strings.

- max:

  non-negative integer (or `NULL`) indicating the maximum number of
  elements to print; set to `getOption("max.print")` if argument is
  `NULL`.

- names:

  a character string specifying the display style for the (column)
  names, as an ANSI SGR parameter string.

- rownames:

  a character string specifying the display style for the row names, as
  an ANSI SGR parameter string.

- escapes:

  a character string specifying the display style for the backslash
  escapes, as an ANSI SGR parameter string.

- display:

  logical scalar indicating whether to optimize the encoding for
  display, not byte-for-byte data transmission.

- style:

  logical scalar indicating whether to apply ANSI terminal escape codes
  to style the output. Ignored when
  [`output_ansi()`](https://krlmlr.github.io/r-utf8/dev/reference/output_utf8.md)
  is `FALSE`.

- utf8:

  logical scalar indicating whether to optimize results for a UTF-8
  capable display, or `NULL` to set as the result of
  [`output_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/output_utf8.md).
  Ignored when
  [`output_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/output_utf8.md)
  is `FALSE`.

## Value

The function returns `x` invisibly.

## Details

`utf8_print()` prints a character object after formatting it with
[`utf8_format()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_format.md).

For ANSI terminal output (when
[`output_ansi()`](https://krlmlr.github.io/r-utf8/dev/reference/output_utf8.md)
is `TRUE`), you can style the row and column names with the `rownames`
and `names` parameters, specifying an ANSI SGR parameter string; see
<https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters>.

## See also

[`utf8_format()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_format.md).

## Examples

``` r
# printing (assumes that output is capable of displaying Unicode 10.0.0)
print(intToUtf8(0x1F600 + 0:79)) # with default R print function
#> [1] "😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏"
utf8_print(intToUtf8(0x1F600 + 0:79)) # with utf8_print, truncates line
#> [1] "😀​😁​😂​😃​😄​😅​😆​😇​😈​😉​😊​😋​😌​😍​😎​😏​😐​😑​😒​😓​😔​😕​😖​😗​😘​😙​😚​😛​😜​😝​😞​😟​😠​😡​😢​😣​…"
utf8_print(intToUtf8(0x1F600 + 0:79), chars = 1000) # higher character limit
#> [1] "😀​😁​😂​😃​😄​😅​😆​😇​😈​😉​😊​😋​😌​😍​😎​😏​😐​😑​😒​😓​😔​😕​😖​😗​😘​😙​😚​😛​😜​😝​😞​😟​😠​😡​😢​😣​😤​😥​😦​😧​😨​😩​😪​😫​😬​😭​😮​😯​😰​😱​😲​😳​😴​😵​😶​😷​😸​😹​😺​😻​😼​😽​😾​😿​🙀​🙁​🙂​🙃​🙄​🙅​🙆​🙇​🙈​🙉​🙊​🙋​🙌​🙍​🙎​🙏​"

# in C locale, output ASCII (same results on all platforms)
oldlocale <- Sys.getlocale("LC_CTYPE")
invisible(Sys.setlocale("LC_CTYPE", "C")) # switch to C locale
utf8_print(intToUtf8(0x1F600 + 0:79))
#> [1] "\U0001f600\U0001f601\U0001f602\U0001f603\U0001f604\U0001f605\U0001f606..."
invisible(Sys.setlocale("LC_CTYPE", oldlocale)) # switch back to old locale

# Mac and Linux only: style the names
# see https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_(Select_Graphic_Rendition)_parameters
utf8_print(matrix(as.character(1:20), 4, 5),
           names = "1;4", rownames = "2;3")
#>      [,1] [,2] [,3] [,4] [,5]
#> [1,] "1"  "5"  "9"  "13" "17"
#> [2,] "2"  "6"  "10" "14" "18"
#> [3,] "3"  "7"  "11" "15" "19"
#> [4,] "4"  "8"  "12" "16" "20"
```
