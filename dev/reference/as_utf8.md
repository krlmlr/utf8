# UTF-8 Character Encoding

UTF-8 text encoding and validation

`as_utf8()` converts a character object from its declared encoding to a
valid UTF-8 character object, or throws an error if no conversion is
possible. If `normalize = TRUE`, then the text gets transformed to
Unicode composed normal form (NFC) after conversion to UTF-8.

`utf8_valid()` tests whether the elements of a character object can be
translated to valid UTF-8 strings.

## Usage

``` r
as_utf8(x, normalize = FALSE)

utf8_valid(x)
```

## Arguments

- x:

  character object.

- normalize:

  a logical value indicating whether to convert to Unicode composed
  normal form (NFC).

## Value

For `as_utf8()`, the result is a character object with the same
attributes as `x` but with `Encoding` set to `"UTF-8"`.

For `utf8_valid()` a logical object with the same `names`, `dim`, and
`dimnames` as `x`.

## See also

[`utf8_normalize()`](https://krlmlr.github.io/r-utf8/dev/reference/utf8_normalize.md),
[`iconv()`](https://rdrr.io/r/base/iconv.html).

## Examples

``` r
# the second element is encoded in latin-1, but declared as UTF-8
x <- c("fa\u00E7ile", "fa\xE7ile", "fa\xC3\xA7ile")
Encoding(x) <- c("UTF-8", "UTF-8", "bytes")

# attempt to convert to UTF-8 (fails)
if (FALSE) as_utf8(x) # \dontrun{}

y <- x
Encoding(y[2]) <- "latin1" # mark the correct encoding
as_utf8(y) # succeeds
#> [1] "façile" "façile" "façile"

# test for valid UTF-8
utf8_valid(x)
#> [1]  TRUE FALSE  TRUE
```
