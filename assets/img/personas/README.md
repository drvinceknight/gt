# Student personas diagram

`main.tex` is a standalone tikz figure showing the five student personas, a
"typical week" flow, and where each student finds help. It is rendered to
`main.png`, which is embedded on the
[Start here](https://vknight.org/gt/start-here/) page.

The page wraps the image in a `.persona-figure` panel (a white card with a
border), so the light figure reads as a deliberate framed inset in both the
light and dark site themes.

## Building

From this directory:

```sh
pdflatex -interaction=nonstopmode main.tex
magick -density 200 main.pdf -background white -alpha remove -alpha off main.png
rm -f main.aux main.log main.pdf
```

The first command produces `main.pdf`; the second rasterises it to `main.png` at
200 DPI on a white background. Re-run both after editing `main.tex` and commit
the updated `main.png`.

Requires a LaTeX distribution (for `pdflatex`) and ImageMagick (for `magick`).
