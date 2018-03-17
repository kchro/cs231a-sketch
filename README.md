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

install potrace
```
brew install libagg pkg-config potrace
git clone https://github.com/flupke/pypotrace.git
cd pypotrace
pip install -r requirements.txt
pip install .
```



## pipeline

1) *Bitmap to SVG*
take a bitmap image and convert it to stroke-based svg

2) ~~Classifier for Features~~
given a window, classify it as a eye, nose, or a mouth
current neural network model classifies with 98-99% accuracy

3a) *Windowing*
slide a window over a face image to do the classification. create bounding boxes over the image where we expect a feature.

3b) *Contouring*
another method of finding the bounding boxes is to identify contours and place bounding boxes around them

4) *Detection*
eliminate unnecessary bounding boxes (non-maximal suppression)

5) ~~Convert the window to 3-stroke-format~~
convert to SVG lines, then to 3-stroke-format
still have to do testing to make sure it works properly

6) *Animation*
animate the SVG components as they are classified:
