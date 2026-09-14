# utf8

*utf8* is an R package for manipulating and printing UTF-8 text that
fixes multiple bugs in R’s UTF-8 handling.

## Goals and non-goals

*utf8* aims to:

- convert character data to UTF-8 from the encoding declared on it, and
  fail loudly when that declaration turns out to be wrong
- normalize text to Unicode composed normal form (NFC), optionally
  case-folding it or applying the compatibility maps for NFKC
- measure and format text by display width, counting wide characters
  such as emoji as two columns and combining marks as none
- print UTF-8 text, emoji included, where R’s own
  [`print()`](https://rdrr.io/r/base/print.html) escapes it, and report
  what the output connection can actually display with
  [`output_utf8()`](https://krlmlr.github.io/utf8/dev/reference/output_utf8.md)
  and
  [`output_ansi()`](https://krlmlr.github.io/utf8/dev/reference/output_utf8.md)
- install everywhere, with no package dependencies beyond R itself

It is explicitly not trying to:

- guess an encoding from the bytes:
  [`as_utf8()`](https://krlmlr.github.io/utf8/dev/reference/as_utf8.md)
  converts from the declared
  [`Encoding()`](https://rdrr.io/r/base/Encoding.html) and throws an
  error when it cannot
- convert text *out of* UTF-8 into some other encoding, which is what
  [`iconv()`](https://rdrr.io/r/base/iconv.html) is for
- read or write files: every function takes a character object that is
  already in your R session
- be a text analysis package: these functions were split off from
  *corpus* in utf8 1.0.0, and tokenization and term statistics stayed
  behind
- model the full range of character locales: only C and UTF-8 are
  handled, and on Windows every non-C locale is treated as UTF-8

## Installation

### Stable version

*utf8* is [available on
CRAN](https://cran.r-project.org/package=utf8 "CRAN Page"). To install
the latest released version, run the following command in R:

``` r

install.packages("utf8")
```

### Development version

To install the latest development version, run the following:

``` r

# install.packages("pak")
pak::pak("krlmlr/utf8")
```

## Usage

``` r

library(utf8)
```

### Validate character data and convert to UTF-8

Use
[`as_utf8()`](https://krlmlr.github.io/utf8/dev/reference/as_utf8.md) to
validate input text and convert to UTF-8 encoding. The function alerts
you if the input text has the wrong declared encoding:

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

Use
[`utf8_normalize()`](https://krlmlr.github.io/utf8/dev/reference/utf8_normalize.md)
to convert to Unicode composed normal form (NFC). Optionally apply
compatibility maps for NFKC normal form or case-fold.

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

On some platforms (including MacOS), the R implementation of
[`print()`](https://rdrr.io/r/base/print.html) uses an outdated version
of the Unicode standard to determine which characters are printable. Use
[`utf8_print()`](https://krlmlr.github.io/utf8/dev/reference/utf8_print.md)
for an updated print function:

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

``` R
@Manual{,
  title = {utf8: Unicode Text Processing},
  author = {Patrick O. Perry},
  note = {R package version 1.2.6},
  url = {https://krlmlr.github.io/utf8/},
}
```
