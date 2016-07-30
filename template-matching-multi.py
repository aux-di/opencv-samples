# -*- coding: utf-8 -*-

import numpy as np
import cv2

# load a color image
img = cv2.imread('images/template-matching-user.jpg', cv2.IMREAD_COLOR)

# transform from RGB to GRAY scale image
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# load template image
template = cv2.imread('images/user.png', cv2.IMREAD_COLOR)

# transform from RGB to GRAY scale image
gray_template = cv2.cvtColor(template, cv2.COLOR_RGB2GRAY)
h, w = gray_template.shape

# template matching
res = cv2.matchTemplate(gray, gray_template, cv2.TM_CCOEFF_NORMED)

# threshold
threshold = 0.99

# select matching points
loc = np.where(res >= threshold)

print loc

# draw rectangles
for pt in zip(*loc[::-1]):
    print pt
    pt2 = (pt[0] + w, pt[1] + h)
    cv2.rectangle(gray, pt, pt2, 0x66)

cv2.imshow('gray', gray)
cv2.imshow('gray template', gray_template)
cv2.waitKey(0)
cv2.destroyAllWindows()
