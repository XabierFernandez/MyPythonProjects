import numpy as np
import cv2 as cv

e1 = cv.getTickCount()

img1 = cv.imread('/home/xabier/Pictures/tiger_1.jpeg')
img2 = cv.imread('/home/xabier/Pictures/tiger_2.jpeg')
img3 = cv.imread('/home/xabier/Pictures/tiger_2_small.jpeg')
dst = cv.addWeighted(img1,0.6,img2,0.5,0)
cv.imshow('dst',dst)
e2 = cv.getTickCount()
time1 = (e2 - e1)/ cv.getTickFrequency()
print('time1 = ',time1)
cv.waitKey(0)
cv.destroyAllWindows()

e1 = cv.getTickCount()

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img3.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img3gray = cv.cvtColor(img3,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img3gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img3_fg = cv.bitwise_and(img3,img3,mask = mask)

# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img3_fg)
img1[0:rows, 0:cols ] = dst
cv.imshow('res',img1)
e2 = cv.getTickCount()
time2 = (e2 - e1)/ cv.getTickFrequency()
print('time2 = ', time2)
cv.waitKey(0)
cv.destroyAllWindows()
print(cv.useOptimized())
