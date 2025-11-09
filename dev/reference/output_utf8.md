# Output Capabilities

Test whether the output connection has ANSI style escape support or
UTF-8 support.

## Usage

``` r
output_ansi()

output_utf8()
```

## Value

A logical scalar indicating whether the output connection supports the
given capability.

## Details

`output_ansi()` tests whether the output connection supports ANSI style
escapes. This is `TRUE` if the connection is a terminal and not the
Windows GUI. Otherwise, it is true if running in RStudio 1.1 or later
with ANSI escapes enabled, provided
[`stdout()`](https://rdrr.io/r/base/showConnections.html) has not been
redirected to another connection by
[`sink()`](https://rdrr.io/r/base/sink.html).

`output_utf8()` tests whether the output connection supports UTF-8. For
most platforms `l10n_info()$"UTF-8"` gives this information, but this
does not give an accurate result for Windows GUIs. To work around this,
we proceed as follows:

- if the character locale (`LC_CTYPE`) is `"C"`, then the result is
  `FALSE`;

- otherwise, if `l10n_info()$"UTF-8"` is `TRUE`, then the result is
  `TRUE`;

- if running on Windows, then the result is `TRUE`;

- in all other cases the result is `FALSE`.

Strictly speaking, UTF-8 support is always available on Windows GUI, but
only a subset of UTF-8 is available (defined by the current character
locale) when the output is redirected by `knitr` or another process.
Unfortunately, it is impossible to set the character locale to UTF-8 on
Windows. Further, the `utf8` package only handles two character locales:
C and UTF-8. To get around this, on Windows, we treat all non-C locales
on that platform as UTF-8. This liberal approach means that characters
in the user's locale never get escaped; others will get output as
`<U+XXXX>`, with incorrect values for
[`utf8_width()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_width.md).

## See also

[`.Platform()`](https://rdrr.io/r/base/Platform.html),
[`isatty()`](https://rdrr.io/r/base/showConnections.html),
[`l10n_info()`](https://rdrr.io/r/base/l10n_info.html),
[`Sys.getlocale()`](https://rdrr.io/r/base/locales.html)

## Examples

``` r
# test whether ANSI style escapes or UTF-8 output are supported
cat("ANSI:", output_ansi(), "\n")
#> ANSI: FALSE 
cat("UTF8:", output_utf8(), "\n")
#> UTF8: TRUE 

# switch to C locale
Sys.setlocale("LC_CTYPE", "C")
#> [1] "C"
cat("ANSI:", output_ansi(), "\n")
#> ANSI: FALSE 
cat("UTF8:", output_utf8(), "\n")
#> UTF8: FALSE 

# switch to native locale
Sys.setlocale("LC_CTYPE", "")
#> [1] "C.UTF-8"

tmp <- tempfile()
sink(tmp) # redirect output to a file
cat("ANSI:", output_ansi(), "\n")
cat("UTF8:", output_utf8(), "\n")
sink() # restore stdout

# inspect the output
readLines(tmp)
#> [1] "ANSI: FALSE " "UTF8: TRUE " 
```
