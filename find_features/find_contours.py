# import the necessary packages
import argparse
import imutils
import cv2
import numpy as np
import numpy as np
import matplotlib.pylab as plt
import operator

#HELPER FUNCTIONS
#green's theorem
def contour_area(vs):
    a = 0
    x0,y0 = vs[0][0]
    for [[x1,y1]] in vs[1:]:
        dx = x1-x0
        dy = y1-y0
        a += 0.5*(y0*dx - x0*dy)
        x0 = x1
        y0 = y1
    return abs(a)

def overlap(r1,r2,margin):
	m = int(margin/2.0)
	x1 = r1[0] - m
	y1 = r1[1] - m
	x2 = r1[0] + r1[2] + m
	y2 = r1[1] + r1[3] + m
	x3 = r2[0] - m
	y3 = r2[1] - m
	x4 = r2[0] + r2[2] + m
	y4 = r2[1] + r2[3] + m
	#print x1,y1,x2,y2
	#print x3,y3,x4,y4
	#if they don't overlap in x coordinates
	if x1 > x4 or x3 > x2:
		return False
	#don't overlap in y coordinates
	elif y1 > y4 or y3 > y2:
		return False
	else:
		return True

def draw_boxes(boxes, color = (255,0,0)):
	for b in boxes:
		(x, y, w, h) = b
		cv2.rectangle(image, (x, y), (x + w, y + h), color, 1)

#LOAD IN IMAGE
image = cv2.imread("face.png")
h,w,_ = np.shape(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
#get actual image size
temp_mask = image < 200
coords = np.argwhere(temp_mask)
x0, y0,_ = coords.min(axis=0)
x1, y1,_ = coords.max(axis=0) + 1   
cropped = image[x0:x1, y0:y1]

#GET CONTOURS
contours = cv2.findContours(thresh.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if imutils.is_cv2() else contours[1]
for (i, c) in enumerate(contours):
    print("\tSize of contour %d: %d" % (i, len(c)))

#GET BOUNDING BOXES
bboxes = []
for c in contours:
    bboxes.append(cv2.boundingRect(c))
original_bboxes = list(bboxes)

#CLEAN UP
#remove bounding boxes bigger than half the size of the drawing
h_real,w_real,_ = np.shape(cropped)
image_area = h_real * w_real
max_feature_size = image_area / 4.0
#print max_feature_size
smaller_boxes = []
for i in range(len(bboxes)):
	b = bboxes[i]
	a = b[2] * b[3]
	#print a
	if a < max_feature_size:
		#print b
		smaller_boxes.append(bboxes[i])
#print smaller_boxes
bboxes = smaller_boxes[:]
#draw_boxes(bboxes[0])

#NON-MAX SUPPRESSION
#a variation on non-max suppression to produce largest boxes
final_boxes = []
#get sorted bounding box areas
bbox_areas = []
for b in bboxes:
	a = b[2] * b[3]
	bbox_areas.append(a)
sorted_areas = sorted(enumerate(bbox_areas), key = operator.itemgetter(1),reverse = True)
#print sorted_areas
for i in range(len(sorted_areas)):
	index = sorted_areas[i][0]
	box = bboxes[i]
	overlap_flag = False
	for j in range(len(final_boxes)):
		f = final_boxes[j]
		if overlap(f,box,0):
			overlap_flag = True
	if not(overlap_flag):
		if len(final_boxes) == 0:
			final_boxes = [box]
		else:
			final_boxes = np.vstack((final_boxes,list(box)))
#print len(final_boxes)
draw_boxes(final_boxes)
#for f in final_b:
#	contours = np.delete(contours,f)

#SAVE SAMPLE IMAGE
#for i in range(len(contours)):
	#cv2.drawContours(image, np.array([contours[i]]), -1, (0,0,255), 5)
cv2.imwrite("result.png",image)
cv2.imwrite("cropped.png",cropped)

#ALTERNATIVE IMPLEMENTATION:
#contour clustering

#SHOW RESULT IN WINDOW
#cv2.namedWindow("output", cv2.WINDOW_NORMAL)
#cv2.imshow("output", image)
#cv2.waitKey(0)
