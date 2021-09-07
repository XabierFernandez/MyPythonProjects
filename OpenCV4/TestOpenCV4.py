import numpy as np
import cv2 as cv

# Load a color image in grayscale
img = cv.imread('messi5.jpg')
print(img.shape)
if img is not None:
    cv.imshow('imagen', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
