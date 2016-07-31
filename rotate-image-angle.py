# -*- coding: utf-8 -*-

import math
import numpy as np
import cv2
from scipy import ndimage

# load a color image
img = cv2.imread('images/rotated.png', cv2.IMREAD_COLOR)

# transform from RGB to GRAY scale image
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# load template image
template = cv2.imread('images/point.png', cv2.IMREAD_COLOR)

# transform from RGB to GRAY scale image
gray_template = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
h, w = gray_template.shape

# template matching
res = cv2.matchTemplate(gray, gray_template, cv2.TM_CCOEFF_NORMED)

# threshold
threshold = 0.99

# select matching points
loc = np.where(res >= threshold)

points = np.empty((0, 2), dtype=int)

# draw rectangles
for pt in zip(*loc[::-1]):
    points = np.append(points, np.array([pt]), axis=0)

    # pt2 = (pt[0] + w, pt[1] + h)
    # cv2.rectangle(gray, pt, pt2, 0x66)

# draw line

if points[0][1] < points[1][1]:
    x1, y1 = points[0]
    x2, y2 = points[1]
else:
    x1, y1 = points[1]
    x2, y2 = points[0]

# cv2.line(gray, (x1, y1), (x2, y2), 0x66)

######################################
# OpenCV rotate
######################################

# angle
rad = math.atan2(y2 - y1, x2 - x1)
deg = rad * 180 / math.pi

print deg

# rotate image
center = tuple(np.array(gray.shape[0:2]) / 2)
scale = 1.0
size = tuple(np.array(gray.shape[0:2]))
rotation_matrix = cv2.getRotationMatrix2D(center, deg, scale)
rotation = cv2.warpAffine(gray, rotation_matrix, (500, 500), flags=cv2.INTER_CUBIC)
print rotation.shape

######################################
# Scipy rotate
######################################

sp = ndimage.rotate(gray, deg, reshape=False)
cv2.imshow('sp', sp)

# template matching again only ROI(200x200)
sp1 = sp[0:200, 0:200]
res = cv2.matchTemplate(sp1, gray_template, cv2.TM_CCOEFF_NORMED)

# threshold
threshold = 0.98

# select matching points
loc = np.where(res >= threshold)

points = np.empty((0, 2), dtype=int)

# draw rectangles
for pt in zip(*loc[::-1]):
    points = np.append(points, np.array([pt]), axis=0)

    pt2 = (pt[0] + w, pt[1] + h)
    cv2.rectangle(sp1, pt, pt2, 0x66)

# cv2.imshow('gray', gray)
# cv2.imshow('rotation', rotation)
cv2.imshow('sp', sp1)
cv2.imshow('gray template', gray_template)
cv2.waitKey(0)
cv2.destroyAllWindows()
