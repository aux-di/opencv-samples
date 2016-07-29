# -*- coding: utf-8 -*-

import numpy as np
import cv2

# 64 x 48
cols = 64
rows = 48

# color image
img = np.zeros((rows, cols, 3), np.uint8)   # all black

# blue
b = 0
g = 0
r = 255

# paint blue 20 x 10
for y in range(10):
    for x in range(20):
        img.itemset((y, x, 0), b)   # blue channel
        img.itemset((y, x, 0), g)   # green channel
        img.itemset((y, x, 0), r)   # red channel

print img[0]    # data of rows[0]

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
