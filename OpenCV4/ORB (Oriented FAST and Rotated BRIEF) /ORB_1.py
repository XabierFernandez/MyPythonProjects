import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# filename = '../data/blox.jpg'
filename = '../data/box_1.jpg'
# filename = '../data/home.jpg'

img0 = cv.imread(filename)
img= cv.cvtColor(img0,cv.COLOR_BGR2GRAY)

# Initiate ORB detector
orb = cv.ORB_create()
# find the keypoints with ORB
kp = orb.detect(img,None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# draw only keypoints location,not size and orientation
img2 = cv.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)

cv.imshow('ret',img2)
cv.waitKey(0)
cv.destroyAllWindows()