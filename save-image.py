# -*- coding: utf-8 -*-

import numpy as np
import cv2

# 64 x 48
cols = 64
rows = 48

# gray scale image
img = np.zeros((rows, cols, 1), np.uint8)   # all black

# paint white 20 x 10
for y in range(10):
    for x in range(20):
        img.itemset((y, x, 0), 255)

# save image
cv2.imwrite('images/saved-image.jpg', img)

