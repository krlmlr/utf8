# The utf8 Package

UTF-8 Text Processing

## Details

Functions for manipulating and printing UTF-8 encoded text:

- [`as_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/as_utf8.md)
  attempts to convert character data to UTF-8, throwing an error if the
  data is invalid;

- [`utf8_valid()`](https://krlmlr.github.io/r-utf8/dev/reference/as_utf8.md)
  tests whether character data is valid according to its declared
  encoding;

- [`utf8_normalize()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_normalize.md)
  converts text to Unicode composed normal form (NFC), optionally
  applying case-folding and compatibility maps;

- [`utf8_encode()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_encode.md)
  encodes a character string, escaping all control characters, so that
  it can be safely printed to the screen;

- [`utf8_format()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_format.md)
  formats a character vector by truncating to a specified character
  width limit or by left, right, or center justifying;

- [`utf8_print()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_print.md)
  prints UTF-8 character data to the screen;

- [`utf8_width()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_width.md)
  measures the display width of UTF-8 character strings (many emoji and
  East Asian characters are twice as wide as other characters);

- [`output_ansi()`](https://krlmlr.github.io/r-utf8/dev/reference/output_utf8.md)
  and
  [`output_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/output_utf8.md)
  test for the output connections capabilities.

For a complete list of functions, use
[`library(help = "utf8")`](https://rdrr.io/r/base/library.html).

## See also

Useful links:

- <https://krlmlr.github.io/utf8/>

- <https://github.com/krlmlr/utf8>

- Report bugs at <https://github.com/krlmlr/utf8/issues>

## Author

**Maintainer**: Kirill Müller <kirill@cynkra.com>
([ORCID](https://orcid.org/0000-0002-1416-3412))

Authors:

- Patrick O. Perry \[copyright holder\]

Other contributors:

- Unicode, Inc. (Unicode Character Database) \[copyright holder, data
  contributor\]
