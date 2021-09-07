import cv2 as cv
import numpy as np

img = cv.imread('../../data/star.jpg')

img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

ret,thresh = cv.threshold(img_gray,127,255,0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)  
cnt = contours[0]

hull = cv.convexHull(cnt,returnPoints = False)
defects = cv.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv.line(img,start,end,[0,255,0],2)
    cv.circle(img,far,5,[0,0,255],-1)

dist = cv.pointPolygonTest(cnt,(150,150),True)
print(dist)

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()