#!/bin/bash

function simplify () {
   IN="guitar_png/$1"
   OUT="guitar_out/$1"
   python simplify.py --img "$IN" --out "$OUT" || exit 1
}
# function call_potrace () {
   # IN="guitar_out/$1"
   # OUT="guitar_svg/$1"
   
   # convert n02676566_9062-2.png bmp:- | mkbitmap - -t 0.3 -o - | potrace --svg --group -t 15 -o - > n02676566_9062-2.svg
   
   # python simplify.py --img "$IN" --out "$OUT" || exit 1
   # convert $1 bmp:- | mkbitmap $1 -t 0.3 -o $1 | potrace --svg --group -t 15 -o - > out.svg
# }

INPUTS=(
   "n02676566_11377-3.png"
   "n02676566_7927-6.png"
   "n02676566_7844-3.png"
   "n02676566_9062-2.png"
)

test -d guitar_out/ || mkdir -p guitar_out/
test -d guitar_svg/ || mkdir -p guitar_svg/
for FILE in "${INPUTS[@]}"; do
   echo -n "Processing ${FILE}..."
   simplify "$FILE"
   echo "Done!"
done



