import numpy as np
import cv2 as cv

img = cv.imread('../../data/test_6.png')

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret,thresh = cv.threshold(imgray,127,255,0)
contours,hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  
cnt = contours[0]


print(hierarchy[0][0][0])
print(contours[0][0][0])

cv.drawContours(img, contours, -1, (0,0,255), 2)

cv.imshow('Centroids',img)
cv.waitKey(0)
cv.destroyAllWindows()