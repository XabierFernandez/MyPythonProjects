import numpy as np
import cv2 as cv
img = cv.imread('../data/messi5.jpg')
res1 = cv.resize(img,None,fx=5, fy=5, interpolation = cv.INTER_CUBIC)
#OR
# height, width = img.shape[:2]
# res2 = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)

cv.imshow('img',res1)
cv.waitKey(0)
cv.destroyAllWindows()