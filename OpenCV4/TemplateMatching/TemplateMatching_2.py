import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../data/ScrewsNuts.jpg',0)
img2 =  img.copy()
template = cv.imread('../data/Screw.jpg',0)

w, h = template.shape[::-1]
res = cv.matchTemplate(img2,template,cv.TM_CCOEFF_NORMED)
threshold = 0.68
loc = np.where( res >= threshold)
print (loc)
for pt in zip(*loc[::-1]):
    cv.rectangle(img2, pt, (pt[0] + w, pt[1] + h), 125, 4)
    
cv.imshow('Resultado',img2)
cv.waitKey(0)
cv.destroyAllWindows()