import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt



img = cv.imread('../../data/home.jpg')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

hist = cv.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
plt.subplot(121)
plt.imshow(hist,interpolation = 'nearest')
plt.subplot(122)
plt.imshow(hsv)
plt.show()