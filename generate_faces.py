from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

FACES_VIDEO = 'faces.mp4'

def crop(im, shape=(256, 256), padding=0):
    # threshold to remove whitespace
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    # white background, black sketch
    _, im2 = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)

    # black background, white sketch
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    kernel = np.ones((5,5), np.uint8)
    dilation = cv2.dilate(thresh, kernel, iterations=1)

    # find contours of non-whitespace
    _, contours, _ = cv2.findContours(dilation,
                                        cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)

    # find the bounding box of all contours
    xx = []
    yy = []
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        xx.append(x)
        xx.append(x+w)
        yy.append(y)
        yy.append(y+h)
    x = min(xx) - padding
    y = min(yy) - padding
    w = max(xx) - min(xx) + 2*padding
    h = max(yy) - min(yy) + 2*padding

    # crop the image
    crop = im2[y:y+h,x:x+w]
    crop = cv2.resize(crop, shape)

    return crop

if __name__ == '__main__':
    # load video
    video = cv2.VideoCapture(FACES_VIDEO)

    # read video frame by frame
    success, image = video.read()
    count = 0
    success = True
    while success:
        # every fifth frame, crop image and save
        if count % 5 == 0:
            image = crop(image, shape=(256, 256), padding=30)
            cv2.imwrite("faces/face_%d.png" % count, image)

        count += 1
        success, image = video.read()
    print count
