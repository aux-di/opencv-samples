# -*- coding: utf-8 -*-

import numpy as np
import cv2

# load a color image
img = cv2.imread('images/lenna.png', cv2.IMREAD_COLOR)

# transform from RGB to GRAY scale image
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# image size
size = tuple(np.array(gray.shape[0:2]))
print size

# center of image
center = tuple(np.array(gray.shape[0:2]) / 2)
print center

# rotate angle(degree)
angle = 30.0

# scale ratio
scale = 1.0

# rotate image
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotation = cv2.warpAffine(gray, rotation_matrix, size, flags=cv2.INTER_CUBIC)

cv2.imshow('gray', gray)
cv2.imshow('rotation', rotation)
cv2.waitKey(0)
cv2.destroyAllWindows()
