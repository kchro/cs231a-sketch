#!/bin/bash

OBJ="face"

function simplify () {
   IN="face_png/$1"
   OUT="face_out/$1"
   python simplify.py --img "$IN" --out "$OUT" || exit 1
}
function convert () {
   IN="face_out/$1"
   OUT_SVG="face_svg/$1.svg"
   OUT_PDF="face_pdf/$1.pdf"
   OUT_PS="face_ps/$1.ps"
   
   convert "$IN" bmp:- | mkbitmap - -t 0.3 -o - | potrace --svg --flat --longcurve -t 15 -o - > "$OUT_SVG"
   convert "$IN" bmp:- | mkbitmap - -t 0.3 -o - | potrace --postscript --cleartext --longcoding -t 15 -o - > "$OUT_PS"
   # convert face_1.png bmp:- | mkbitmap - -t 0.3 -o - | potrace --backend pdf --cleartext --longcoding --longcurve -t 15 -o - > face_1.svg
   # convert face_1.png bmp:- | mkbitmap - -t 0.3 -o - | potrace --postscript --cleartext --longcoding -t 15 -o - > face_1.ps
   
   # python simplify.py --img "$IN" --out "$OUT" || exit 1
   # convert $1 bmp:- | mkbitmap $1 -t 0.3 -o $1 | potrace --svg --group -t 15 -o - > out.svg
}

INPUTS=(
   "face_1.png"
   "face_2.png"
   "face_3.png"
)

test -d face_out/ || mkdir -p face_out/
test -d face_svg/ || mkdir -p face_svg/
test -d face_ps/ || mkdir -p face_ps/
for FILE in "${INPUTS[@]}"; do
   echo -n "Processing ${FILE}..."
   # simplify "$FILE"
   convert "$FILE"
   echo "Done!"
done



