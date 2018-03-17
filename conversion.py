import numpy as np
np.set_printoptions(linewidth=np.nan, precision=3)
import cv2
import potrace
import matplotlib.pyplot as plt
from face_data import load_faces

def lines_to_strokes(lines):
    strokes = [[0,0,0]]

    # each line is (2 x n)
    for line in lines:
        n = len(line[0])
        # for each xy coordinate pair, append
        for i in range(n):
            eos = 0 if i < n-1 else 1
            strokes.append([line[0][i], line[1][i], eos])
    strokes = np.array(strokes)

    # calculate the delta
    strokes[1:, 0:2] -= strokes[:-1, 0:2]
    return strokes[1:, :]

def convert_to_3_stroke(im):
    # black background, white sketch
    _, thresh = cv2.threshold(im, 200, 255, cv2.THRESH_BINARY_INV)

    # dilate -> erode
    kernel = np.ones((3,3), np.uint8)
    im = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Get inverted boolean matrix:
    # potrace only works with boolean images
    data = im == 0

    # Create a bitmap from the array
    bmp = potrace.Bitmap(data)
    path = bmp.trace()

    # get the xy coordinates for each curve
    lines = [curve.tesselate().T for curve in path]

    # get the 3 stroke format
    strokes = lines_to_strokes(lines[1:])

    return strokes

if __name__ == '__main__':
    for face in load_faces(n=10):
        im = cv2.imread(face, 0)
        # black background, white sketch
        _, thresh = cv2.threshold(im, 200, 255, cv2.THRESH_BINARY_INV)
        kernel = np.ones((3,3), np.uint8)
        im = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        # Get inverted boolean matrix:
        # 1 if black, 0 if white
        data = im == 0

        # Create a bitmap from the array
        bmp = potrace.Bitmap(data)
        path = bmp.trace()

        lines = [curve.tesselate().T for curve in path]

        strokes = lines_to_strokes(lines[1:])
        print strokes
