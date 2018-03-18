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



## pipeline (TO DO LIST)

1) *Bitmap to SVG*
take a bitmap image and convert it to stroke-based svg
-apply RDP simplification
-apply normalization (use 46.5 for 256 size images)

2) ~~Classifier for Features ~~ given a window, classify it as a eye, nose, or a mouth
current neural network model classifies with 98-99% accuracy!
output prediction
output confidence score

3a) *Windowing*
slide a window over a face image to do the classification. create bounding boxes over the image where we expect a feature.
output the bounding box

3b) *Contouring*
another method of finding the bounding boxes is to identify contours and place bounding boxes around them
output bounding boxes

4) *Detection*
eliminate unnecessary bounding boxes (non-maximal suppression)
done for contouring 

5) ~~Convert the window to 3-stroke-format~~
convert to SVG lines, then to 3-stroke-format
still have to do testing to make sure it works properly

6) *Animation*
animate the SVG components as they are classified:

PRESENTATION TO DO

diagram/chart of prediction numbers (I haven't totally analyzed what they mean, or how far they range)

neural net diagrams

classifier error analysis: make a diagram of high score classifications with varying stroke styles

contouring success chart

windowing success chart

animation

FINAL PAPER TO DO

