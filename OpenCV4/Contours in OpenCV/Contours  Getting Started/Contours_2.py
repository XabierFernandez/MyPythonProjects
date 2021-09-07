import numpy as np
import cv2 as cv

img = cv.imread('../../data/test_4.png',0)

ret,thresh = cv.threshold(img,127,255,0)
contours,hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]

M = cv.moments(cnt)
A = cv.contourArea(cnt)
perimeter = cv.arcLength(cnt,True)

print('Moment = ', M )
print('Area = ', A )
print('Perimeter = ', perimeter )

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print('CX = ', cx)
print('CY =', cy)



cv.circle(img, (cx, cy), 3, (0, 0, 255), -1)


cv.imshow('Centroids',img)
cv.waitKey(0)
cv.destroyAllWindows()