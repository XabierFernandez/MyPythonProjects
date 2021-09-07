import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../data/messi5.jpg',0)
blur = cv.GaussianBlur(img,(3,3),0)

edges = cv.Canny(blur,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), 
plt.xticks([]), 
plt.yticks([])

plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), 
plt.xticks([]), 
plt.yticks([])
plt.show()