# Changelog

## utf8 1.2.6.9006 (2025-11-17)

### Continuous integration

- Install binaries from r-universe for dev workflow
  ([\#90](https://github.com/krlmlr/utf8/issues/90)).

## utf8 1.2.6.9005 (2025-11-12)

### Continuous integration

- Fix reviewdog and add commenting workflow
  ([\#88](https://github.com/krlmlr/utf8/issues/88)).

## utf8 1.2.6.9004 (2025-11-10)

### Continuous integration

- Sync ([\#86](https://github.com/krlmlr/utf8/issues/86)).

## utf8 1.2.6.9003 (2025-09-05)

### Chore

- Auto-update from GitHub Actions
  ([\#84](https://github.com/krlmlr/utf8/issues/84)).

## utf8 1.2.6.9002 (2025-08-05)

### Continuous integration

- Format with air, check detritus, better handling of `extra-packages`
  ([\#82](https://github.com/krlmlr/utf8/issues/82)).

## utf8 1.2.6.9001 (2025-06-13)

### Continuous integration

- Try to break R 4.1 builds by adding configure.win.

## utf8 1.2.6.9000 (2025-06-09)

- Switching to development version.

## utf8 1.2.6 (2025-06-08)

CRAN release: 2025-06-08

### Chore

- Format with air.

### Continuous integration

- Enhance permissions for workflow
  ([\#77](https://github.com/krlmlr/utf8/issues/77)).

### Documentation

- Fix URL ([@olivroy](https://github.com/olivroy),
  [\#78](https://github.com/krlmlr/utf8/issues/78)).

## utf8 1.2.5 (2025-05-01)

CRAN release: 2025-05-01

### Features

- Strict argument checking for
  [`utf8_format()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_format.md)
  and
  [`utf8_print()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_print.md),
  no extra arguments allowed.

### Chore

- Replace `[v]sprintf()` with `[v]snprintf()`
  ([\#67](https://github.com/krlmlr/utf8/issues/67)).

- Add direct include for `snprintf()`
  ([@MichaelChirico](https://github.com/MichaelChirico),
  [\#43](https://github.com/krlmlr/utf8/issues/43)).

- Add ellipsis before optional args
  ([\#74](https://github.com/krlmlr/utf8/issues/74)).

### Documentation

- Show NEWS on CRAN page
  ([\#42](https://github.com/krlmlr/utf8/issues/42),
  [\#71](https://github.com/krlmlr/utf8/issues/71)).

- Add pkgdown reference index.

- Use roxygen2 ([\#68](https://github.com/krlmlr/utf8/issues/68),
  [\#69](https://github.com/krlmlr/utf8/issues/69)) with Markdown.

### Performance

- Check interrupt every 1024 calls, avoids a division in tight loops.

## utf8 1.2.4 (2023-10-16)

CRAN release: 2023-10-22

- Fix compatibility with macOS 14
  ([\#39](https://github.com/krlmlr/utf8/issues/39)).

## utf8 1.2.3 (2023-01-30)

CRAN release: 2023-01-31

### Features

- Support Unicode 14.

### Chore

- Update maintainer e-mail address.

- Fix compiler warnings ([@Antonov548](https://github.com/Antonov548),
  [\#37](https://github.com/krlmlr/utf8/issues/37)).

## utf8 1.2.2 (2021-07-24)

CRAN release: 2021-07-24

- Reenable all tests.
- [`utf8_width()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_width.md)
  now reports correct widths for narrow emojis
  ([\#9](https://github.com/krlmlr/utf8/issues/9)).

## utf8 1.2.1 (2021-03-10)

CRAN release: 2021-03-12

- Use Unicode and Emoji standards version 13.0 via upgrade to latest
  `utf8lite`.
- Silence test on macOS.

## utf8 1.1.4 (2018-05-24)

CRAN release: 2018-05-24

### BUG FIXES

- Fix build on Solaris ([\#7](https://github.com/krlmlr/utf8/issues/7),
  reported by [@krlmlr](https://github.com/krlmlr)).

- Fix rendering of emoji ZWJ sequences like
  `"\U1F469\U200D\U2764\UFE0F\U200D\U1F48B\U200D\U1F469"`.

## utf8 1.1.3 (2018-01-03)

CRAN release: 2018-01-03

### MINOR IMPROVEMENTS

- Make
  [`output_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/output_utf8.md)
  always return `TRUE` on Windows, so that characters in the user’s
  native locale don’t get escaped by
  [`utf8_encode()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_encode.md).
  The downside of this change is that on Windows,
  [`utf8_width()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_width.md)
  reports the wrong values for characters outside the user’s locale when
  [`stdout()`](https://rdrr.io/r/base/showConnections.html) is
  redirected by `knitr` or another process.

- When truncating long strings strings via
  [`utf8_format()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_format.md),
  use an ellipsis that is printable in the user’s native locale
  (`"\u2026" or`“…”\`).

## utf8 1.1.2 (2017-12-14)

CRAN release: 2017-12-14

### BUG FIXES

- Fix bug in
  [`utf8_format()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_format.md)
  with non-`NULL` `width` argument.

## utf8 1.1.1 (2017-11-28)

CRAN release: 2017-11-29

### BUG FIXES

- Fix PROTECT bug in
  [`as_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/as_utf8.md).

## utf8 1.1.0 (2017-11-20)

CRAN release: 2017-11-20

### NEW FEATURES

- Added
  [`output_ansi()`](https://krlmlr.github.io/r-utf8/dev/reference/output_utf8.md)
  and
  [`output_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/output_utf8.md)
  functions to test for output capabilities.

### MINOR IMPROVEMENTS

- Add `utf8` argument to
  [`utf8_encode()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_encode.md),
  [`utf8_format()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_format.md),
  [`utf8_print()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_print.md),
  and
  [`utf8_width()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_width.md)
  for precise control over assumed output capabilities; defaults to the
  result of
  [`output_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/output_utf8.md).

- Add ability to style backslash escapes with the `escapes` arguments to
  [`utf8_encode()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_encode.md)
  and
  [`utf8_print()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_print.md).
  Switch from “faint” styling to no styling by default.

- Slightly reword error messages for
  [`as_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/as_utf8.md).

- Fix (spurious) `rchk` warnings.

### BUG FIXES

- Fix bug in
  [`utf8_width()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_width.md)
  determining width of non-ASCII strings when `LC_CTYPE=C`.

### DEPRECATED AND DEFUNCT

- No longer export the C version of
  [`as_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/as_utf8.md)
  (the R version is still present).

## utf8 1.0.0 (2017-11-06)

CRAN release: 2017-11-07

### NEW FEATURES

- Split off functions
  [`as_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/as_utf8.md),
  [`utf8_valid()`](https://krlmlr.github.io/r-utf8/dev/reference/as_utf8.md),
  [`utf8_normalize()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_normalize.md),
  [`utf8_encode()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_encode.md),
  [`utf8_format()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_format.md),
  [`utf8_print()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_print.md),
  and
  [`utf8_width()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_width.md)
  from [corpus](http://corpustext.com/ "corpus: Text Corpus Analysis")
  package.

- Added special handling for Unicode grapheme clusters in formatting and
  width measurement functions.

- Added ANSI styling to escape sequences.

- Added ability to style row and column names in
  [`utf8_print()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_print.md).
