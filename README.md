
<!-- README.md and index.md are generated from README.Rmd. Please edit that file. -->

# utf8

<!-- badges: start -->

[![rcc](https://github.com/patperry/r-utf8/workflows/rcc/badge.svg)](https://github.com/krlmlr/utf8/actions)
[![Coverage Status](https://codecov.io/github/patperry/r-utf8/coverage.svg?branch=main "Code Coverage")](https://app.codecov.io/github/patperry/r-utf8?branch=main "Code Coverage")
[![CRAN Status](https://www.r-pkg.org/badges/version/utf8 "CRAN Page")](https://cran.r-project.org/package=utf8 "CRAN Page")
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg "Apache License, Version 2.0")](https://www.apache.org/licenses/LICENSE-2.0.html "Apache License, Version 2.0")
[![CRAN RStudio Mirror Downloads](https://cranlogs.r-pkg.org/badges/utf8 "CRAN Downloads")](https://cran.r-project.org/package=utf8 "CRAN Page")
<!-- badges: end -->

*utf8* is an R package for manipulating and printing UTF-8 text that fixes multiple bugs in R's UTF-8 handling.

## Installation

### Stable version

*utf8* is [available on CRAN](https://cran.r-project.org/package=utf8 "CRAN Page"). To install the latest released version,
run the following command in R:

``` r
install.packages("utf8")
```

### Development version

To install the latest development version, run the following:

``` r
# install.packages("pak")
pak::pak("patperry/r-utf8")
```

## Usage

``` r
library(utf8)
```

### Validate character data and convert to UTF-8

Use `as_utf8()` to validate input text and convert to UTF-8 encoding. The
function alerts you if the input text has the wrong declared encoding:

``` r
# second entry is encoded in latin-1, but declared as UTF-8
x <- c("fa\u00E7ile", "fa\xE7ile", "fa\xC3\xA7ile")
Encoding(x) <- c("UTF-8", "UTF-8", "bytes")
as_utf8(x) # fails
#> Error in `as_utf8()`:
#> ! entry 2 has wrong Encoding; marked as "UTF-8" but leading byte 0xE7 followed by invalid continuation byte (0xdeadbeef) at position 4

# mark the correct encoding
Encoding(x[2]) <- "latin1"
as_utf8(x) # succeeds
#> [1] "façile" "façile" "façile"
```

### Normalize data

Use `utf8_normalize()` to convert to Unicode composed normal form (NFC).
Optionally apply compatibility maps for NFKC normal form or case-fold.

``` r
# three ways to encode an angstrom character
(angstrom <- c("\u00c5", "\u0041\u030a", "\u212b"))
#> [1] "Å" "Å" "Å"
utf8_normalize(angstrom) == "\u00c5"
#> [1] TRUE TRUE TRUE

# perform full Unicode case-folding
utf8_normalize("Größe", map_case = TRUE)
#> [1] "grösse"

# apply compatibility maps to NFKC normal form
# (example from https://twitter.com/aprilarcus/status/367557195186970624)
utf8_normalize("𝖸𝗈 𝐔𝐧𝐢𝐜𝐨𝐝𝐞 𝗅 𝗁𝖾𝗋𝖽 𝕌 𝗅𝗂𝗄𝖾 𝑡𝑦𝑝𝑒𝑓𝑎𝑐𝑒𝑠 𝗌𝗈 𝗐𝖾 𝗉𝗎𝗍 𝗌𝗈𝗆𝖾 𝚌𝚘𝚍𝚎𝚙𝚘𝚒𝚗𝚝𝚜 𝗂𝗇 𝗒𝗈𝗎𝗋 𝔖𝔲𝔭𝔭𝔩𝔢𝔪𝔢𝔫𝔱𝔞𝔯𝔶 𝔚𝔲𝔩𝔱𝔦𝔩𝔦𝔫𝔤𝔳𝔞𝔩 𝔓𝔩𝔞𝔫𝔢 𝗌𝗈 𝗒𝗈𝗎 𝖼𝖺𝗇 𝓮𝓷𝓬𝓸𝓭𝓮 𝕗𝕠𝕟𝕥𝕤 𝗂𝗇 𝗒𝗈𝗎𝗋 𝒇𝒐𝒏𝒕𝒔.",
               map_compat = TRUE)
#> [1] "Yo Unicode l herd U like typefaces so we put some codepoints in your Supplementary Wultilingval Plane so you can encode fonts in your fonts."
```

### Print emoji

On some platforms (including MacOS), the R implementation of `print()` uses an
outdated version of the Unicode standard to determine which characters are
printable. Use `utf8_print()` for an updated print function:

``` r
print(intToUtf8(0xdeadbeefF600 + 0:79)) # with default R print function
#> [1] "😀😁😂😃😄😅😆😇😈😉😊😋😌😍😎😏😐😑😒😓😔😕😖😗😘😙😚😛😜😝😞😟😠😡😢😣😤😥😦😧😨😩😪😫😬😭😮😯😰😱😲😳😴😵😶😷😸😹😺😻😼😽😾😿🙀🙁🙂🙃🙄🙅🙆🙇🙈🙉🙊🙋🙌🙍🙎🙏"

utf8_print(intToUtf8(0xdeadbeefF600 + 0:79)) # with utf8_print, truncates line
#> [1] "😀​😁​😂​😃​😄​😅​😆​😇​😈​😉​😊​😋​😌​😍​😎​😏​😐​😑​😒​😓​😔​😕​😖​😗​😘​😙​😚​😛​😜​😝​😞​😟​😠​😡​😢​😣​…"

utf8_print(intToUtf8(0xdeadbeefF600 + 0:79), chars = 1000) # higher character limit
#> [1] "😀​😁​😂​😃​😄​😅​😆​😇​😈​😉​😊​😋​😌​😍​😎​😏​😐​😑​😒​😓​😔​😕​😖​😗​😘​😙​😚​😛​😜​😝​😞​😟​😠​😡​😢​😣​😤​😥​😦​😧​😨​😩​😪​😫​😬​😭​😮​😯​😰​😱​😲​😳​😴​😵​😶​😷​😸​😹​😺​😻​😼​😽​😾​😿​🙀​🙁​🙂​🙃​🙄​🙅​🙆​🙇​🙈​🙉​🙊​🙋​🙌​🙍​🙎​🙏​"
```

## Citation

Cite *utf8* with the following BibTeX entry:

    @Manual{,
      title = {utf8: Unicode Text Processing},
      author = {Patrick O. Perry},
      note = {R package version 1.2.6.9020},
      url = {https://krlmlr.github.io/utf8/},
    }

------------------------------------------------------------------------

## Contributing

The project maintainer welcomes contributions in the form of feature requests,
bug reports, comments, unit tests, vignettes, or other code. If you'd like to
contribute, either

- fork the repository and submit a pull request

- [file an issue](https://github.com/krlmlr/utf8/issues "Issues");

- or contact the maintainer via e-mail.

This project is released with a [Contributor Code of Conduct](https://github.com/krlmlr/utf8/blob/main/CONDUCT.md "Contributor Code of Conduct"),
and if you choose to contribute, you must adhere to its terms.
