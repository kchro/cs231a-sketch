# cs231a-sketch
CS231A Project (Gary Yu, Cynthia Hua, Jeff Hara)

## todo

## pipeline

1) *Bitmap to SVG*
take a bitmap image and convert it to stroke-based svg

2) *Classifier for Features*
given a window, classify it as a eye, nose, or a mouth

3) *Windowing*
slide a window over a face image to do the classification. create bounding boxes over the image where we expect a
feature.

4) *Detection*
eliminate unnecessary bounding boxes (non-maximal suppression)

5) *Mapping to SVG*
identify the corresponding SVG components to animate

6) *Animation*
animate the SVG components as they are classified:
