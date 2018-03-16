# cs231a-sketch
CS231A Project (Gary Yu, Cynthia Hua, Jeff Hara)

## todo

### jeff:
I added files to generate the faces in case that's useful.

```
mkdir faces
chmod +x download_faces.sh
./download_faces.sh
```

## pipeline

1) *Bitmap to SVG*
take a bitmap image and convert it to stroke-based svg

2) *Classifier for Features*
given a window, classify it as a eye, nose, or a mouth

3) *Windowing*
slide a window over a face image to do the classification. create bounding boxes over the image where we expect a feature.

4) *Detection*
eliminate unnecessary bounding boxes (non-maximal suppression)

5) *Mapping to SVG*
identify the corresponding SVG components to animate

6) *Animation*
animate the SVG components as they are classified:
