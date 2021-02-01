import numpy as np
import cv2 as cv

img = cv.imread('../data/home.jpg')
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)

surf = cv.xfeatures2d.SURF_create(400)
# kp, des = surf.detectAndCompute(gray,None)

# print(len(kp))
# print(surf.getHessianThreshold())
# print(surf.setHessianThreshold(50000))
surf.setUpright(True)
surf.setExtended(True)
print(surf.getUpright())
print(surf.getExtended())
print(surf.descriptorSize())


kp, des = surf.detectAndCompute(gray,None)
print(des.shape)


img2 = cv.drawKeypoints(gray,kp,None,(255,0,0),4)

cv.imshow('ret',img2)
cv.waitKey(0)
cv.destroyAllWindows()