import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../../data/home.jpg',0)
hist = cv.calcHist([img],[0],None,[256],[0,256])

plt.hist(img.ravel(),256,[0,256])
plt.show()