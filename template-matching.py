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

# template matching
res = cv2.matchTemplate(gray, gray_template, cv2.TM_CCOEFF_NORMED)

print len(res)

(minval, maxval, minloc, maxloc) = cv2.minMaxLoc(res)

print "({0}, {1}) score = {2}".format(maxloc[0], maxloc[1], maxval)
(h, w) = gray_template.shape

rect_1 = (maxloc[0], maxloc[1])
rect_2 = (maxloc[0] + w, maxloc[1] + h)
print "({0}, {1}) score = {2}\n".format(maxloc[0], maxloc[1], maxval)
print "size ({0}, {1})\n".format(w, h)

cv2.rectangle(gray, rect_1, rect_2, 0x99)

cv2.imshow('gray', gray)
cv2.imshow('gray template', gray_template)
cv2.waitKey(0)
cv2.destroyAllWindows()
