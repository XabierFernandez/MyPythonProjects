import numpy as np
import cv2 as cv
import os

filePath = '../../data/test_4.png'
bFileExist = os.path.isfile(filePath)
im = cv.imread(filePath)

if bFileExist:
    try:
        imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
        ret, thresh = cv.threshold(imgray, 127, 255, 0)
        
        contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        
        cv.drawContours(im, contours, -1, (0,255,0), 3)
        
        cv.imshow('Contour',im)
        cv.waitKey(0)
        cv.destroyAllWindows()
    except cv.error as e:
        print('file doesn\'t exist\n\n',e)