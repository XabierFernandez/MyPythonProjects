import numpy as np
import cv2 as cv

img0 = cv.imread('../../data/test_4.png')
img = cv.cvtColor(img0, cv.COLOR_BGR2GRAY)

x,y,w,h = cv.boundingRect(img)
aspect_ratio = float(w)/h

ret,thresh = cv.threshold(img,127,255,0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)        
cnt = contours[0]

# ------------------------------
area = cv.contourArea(cnt)
# ------------------------------
x,y,w,h = cv.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area


hull = cv.convexHull(cnt)
hull_area = cv.contourArea(hull)
solidity = float(area)/hull_area
equi_diameter = np.sqrt(4*area/np.pi)

(x,y),(MA,ma),angle = cv.fitEllipse(cnt)


mask = np.zeros(img0.shape,np.uint8)
cv.drawContours(mask,[cnt],0,[0,125,0],-1)
pixelpoints = np.transpose(np.nonzero(mask))
#pixelpoints = cv.findNonZero(mask)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(img)
mean_val = cv.mean(img)

leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

cv.circle(mask, leftmost, 3, (0, 0, 255), -1)
cv.circle(mask, rightmost, 3, (0, 0, 255), -1)
cv.circle(mask, topmost, 3, (0, 0, 255), -1)
cv.circle(mask, bottommost, 3, (0, 0, 255), -1)

print('Aspcet ratio = ', aspect_ratio)
print('Extent = ', extent)
print('Solidity = ', solidity)
print('Equivalent diameter = ', equi_diameter)
print('Angle = ', angle)

print('Min value = ', min_val)
print('Max value = ', max_val)
print('Mean value = ', mean_val)

cv.imshow('Original',mask)
cv.waitKey(0)
cv.destroyAllWindows()