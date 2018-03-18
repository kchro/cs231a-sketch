# cs231a-sketch
CS231A Project (Gary Yu, Cynthia Hua, Jeff Hara)

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



## pipeline (TO DO LIST)

### *Bitmap to SVG*
- see **svg_conversion.ipynb**
- ~~take a bitmap image and convert it to stroke-based svg~~
- ~~apply RDP simplification~~
- apply normalization (use 46.5 for 256 size images)

### ~~Classifier for Features~~
- see **neuralnet/demo.ipynb**
- given a window, classify it as a eye, nose, or a mouth
- *(current neural network model classifies with 98-99% accuracy!)*
- ~~output prediction~~
- ~~output confidence score~~

### *Method 1: Windowing*
- see **neuralnet_test_harness.ipynb**
- ~~slide a window over a face image to do the classification~~
- create bounding boxes over the image where we expect a feature.
- output the bounding box

### *Method 2: Contouring*
- another method of finding the bounding boxes is to identify contours and place bounding boxes around them
- output bounding boxes

### *Detection*
- Method 1: eliminate unnecessary bounding boxes (non-maximal suppression)
- ~~Method 2: done~~

### ~~Convert the window to 3-stroke-format~~
- ~~convert to SVG lines, then to 3-stroke-format~~
- ~~still have to do testing to make sure it works properly~~

### *Animation*
- animate the SVG components as they are classified

## PRESENTATION TO DO

- diagram/chart of prediction numbers (I haven't totally analyzed what they mean, or how far they range)

- neural net diagrams

- classifier error analysis: make a diagram of high score classifications with varying stroke styles

- contouring success chart

- windowing success chart

- animation

## FINAL PAPER TO DO
