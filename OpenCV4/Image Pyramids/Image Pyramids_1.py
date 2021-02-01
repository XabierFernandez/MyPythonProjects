import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../data/messi5.jpg')
higher_reso2 = cv.pyrUp(img)
lower_reso = cv.pyrDown(higher_reso2)


cv.imshow('Original',img)
cv.imshow('lower_reso',lower_reso)
cv.imshow('higher_reso2',higher_reso2)
cv.waitKey(0)
cv.destroyAllWindows()