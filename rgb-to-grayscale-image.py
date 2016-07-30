# -*- coding: utf-8 -*-

import numpy as np
import cv2

# load a color image
img = cv2.imread('images/raspberries.jpg', cv2.IMREAD_COLOR)

# transform from RGB to GRAY scale image
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow('color', img)
cv2.imshow('gray', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
