import numpy as np
import cv2 as cv

img0 = cv.imread('../../data/test_4.png')
img = cv.cvtColor(img0, cv.COLOR_BGR2GRAY)

ret,thresh = cv.threshold(img,127,255,0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)        
cnt = contours[0]

x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(img0,(x,y),(x+w,y+h),(0,255,0),2)

rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img0,[box],0,(0,0,255),2)

(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv.circle(img0,center,radius,(0,255,0),2)

ellipse = cv.fitEllipse(cnt)
cv.ellipse(img0,ellipse,(0,255,0),2)


rows,cols = img0.shape[:2]
[vx,vy,x,y] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv.line(img0,(cols-1,righty),(0,lefty),(0,255,0),2)

cv.imshow('Centroids',img0)
cv.waitKey(0)
cv.destroyAllWindows()