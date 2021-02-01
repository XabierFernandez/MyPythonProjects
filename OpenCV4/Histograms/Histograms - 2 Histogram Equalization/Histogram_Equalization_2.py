import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../../data/wiki.jpg',0)

# CLAHE (Contrast Limited Adaptive Histogram Equalization)
# create a CLAHE object (Arguments are optional).
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

plt.subplot(121), plt.imshow(img, 'gray')
plt.subplot(122), plt.imshow(cl1,'gray')
plt.show()
