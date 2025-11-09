# Text Normalization

Transform text to normalized form, optionally mapping to lowercase and
applying compatibility maps.

## Usage

``` r
utf8_normalize(
  x,
  ...,
  map_case = FALSE,
  map_compat = FALSE,
  map_quote = FALSE,
  remove_ignorable = FALSE
)
```

## Arguments

- x:

  character object.

- ...:

  These dots are for future extensions and must be empty.

- map_case:

  a logical value indicating whether to apply Unicode case mapping to
  the text. For most languages, this transformation changes uppercase
  characters to their lowercase equivalents.

- map_compat:

  a logical value indicating whether to apply Unicode compatibility
  mappings to the characters, those required for NFKC and NFKD normal
  forms.

- map_quote:

  a logical value indicating whether to replace curly single quotes and
  Unicode apostrophe characters with ASCII apostrophe (U+0027).

- remove_ignorable:

  a logical value indicating whether to remove Unicode "default
  ignorable" characters like zero-width spaces and soft hyphens.

## Value

The result is a character object with the same attributes as `x` but
with `Encoding` set to `"UTF-8"`.

## Details

`utf8_normalize()` converts the elements of a character object to
Unicode normalized composed form (NFC) while applying the character maps
specified by the `map_case`, `map_compat`, `map_quote`, and
`remove_ignorable` arguments.

## See also

[`as_utf8()`](https://krlmlr.github.io/r-utf8/dev/reference/as_utf8.md).

## Examples

``` r
angstrom <- c("\u00c5", "\u0041\u030a", "\u212b")
utf8_normalize(angstrom) == "\u00c5"
#> [1] TRUE TRUE TRUE
```
