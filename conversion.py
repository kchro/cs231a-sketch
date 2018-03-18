import numpy as np
np.set_printoptions(linewidth=np.nan, precision=3)
import cv2
import potrace
import matplotlib.pyplot as plt
from rdp import rdp
from face_data import load_faces

def lines_to_strokes(lines):
    """
    mostly taken the SketchRNN source code
    main difference is formatting of lines parameter

    params:
        lines       an array of lines, where each line
                    is a (2 x n) matrix of x, y pairs

    returns:
        strokes     an array of (dx, dy, eos) for all
                    the paths in lines
    """
    strokes = [[0,0,0]]

    # each line is (2 x n)
    for line in lines:
        n = len(line)

        # for each xy coordinate pair, append
        for i in range(n):
            eos = 0 if i < n-1 else 1
            strokes.append([line[i][0], line[i][1], eos])

    strokes = np.array(strokes, dtype=np.float32)

    # calculate the delta
    strokes[1:, 0:2] -= strokes[:-1, 0:2]
    return strokes[1:, :]

def convert_to_3_stroke(im):
    """
    params:
        im          image

    method:
        1)  dilate and erode the image to
            group line segments together
        2)  convert to bitmap
        3)  trace bitmap to SVG
        4)  convert SVG to 3-stroke format

    returns:
        strokes     3-stroke format
    """
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

    plt.imshow(data, cmap=plt.cm.gray)

    # get the xy coordinates for each curve
    lines = []
    for i, curve in enumerate(path):
        # for some reason, the first curve
        # is always weird
        if i == 0:
            continue

        line = curve.tesselate()

        # perform Ramer-Douglas-Peuker algorithm
        line = rdp(line, epsilon=1)

        x, y = line.T
        plt.plot(x, y, c='red')

        lines.append(line)

    plt.show()

    # get the 3 stroke format
    strokes = lines_to_strokes(lines)

    return strokes

def get_curves(im, kernel_size=3):
    """
    params:
        im          image
    returns:
        lines       xy coordinates of lines
    """
    # black background, white sketch
    _, thresh = cv2.threshold(im, 200, 255, cv2.THRESH_BINARY_INV)

    # dilate -> erode
    kernel = np.ones((kernel_size,kernel_size), np.uint8)
    im2 = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # Get inverted boolean matrix:
    # potrace only works with boolean images
    data = im2 == 0

    # Create a bitmap from the array
    bmp = potrace.Bitmap(data)
    paths = bmp.trace()

    lines = []
    for i, curve in enumerate(paths):
        if i == 0:
            continue
        line = curve.tesselate()
        line = rdp(line, epsilon=1)
        lines.append(line)

    return lines

def get_window_3_stroke(lines, im, j, i, window_size=100):
    # plt.imshow(im[j:j+window_size, i:i+window_size],
    #            cmap=plt.cm.gray)

    new_lines = []
    for line in lines:
        # print line

        inbounds = []
        for x, y in line:
            if (x > i and x < i+window_size) and \
               (y > j and y < j+window_size):

               inbounds.append([x, y])
        inbounds = np.array(inbounds)

        if len(inbounds) > 0:
            new_lines.append(inbounds)
            # X, Y = inbounds.T
            # plt.plot(X, Y, c='red')

    # plt.show()

    strokes = lines_to_strokes(new_lines)
    return strokes

if __name__ == '__main__':
    for face in load_faces(n=5):
        im = cv2.imread(face, 0)
        # strokes = convert_to_3_stroke(im)
        lines = get_curves(im)
        lines = get_window_3_stroke(lines, im, 0, 0)
        # draw_strokes(strokes)
