import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../data/j.png',0)



img1 = cv.imread('../data/opening.png',0)
img2 = cv.imread('../data/closing.png',0)
img3 = cv.imread('../data/closing_with_scratches.png',0)
img4 = cv.imread('../data/gradient_1.png',0)


kernel = np.ones((5,5),np.uint8)
kernel_1 = np.ones((9,9),np.uint8)

erosion = cv.erode(img,kernel,iterations = 1)
dilation = cv.dilate(img,kernel,iterations = 1)

opening = cv.morphologyEx(img1, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img2, cv.MORPH_CLOSE, kernel)
closing_scratches = cv.morphologyEx(img3, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(img4, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(img4, cv.MORPH_TOPHAT, kernel_1)
blackhat = cv.morphologyEx(img4, cv.MORPH_BLACKHAT, kernel_1)


# Rectangular Kernel
cv.getStructuringElement(cv.MORPH_RECT,(5,5))
np.array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=np.uint8)
# Elliptical Kernel
cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
np.array([[0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0]], dtype=np.uint8)
# Cross-shaped Kernel
cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
np.array([[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0]], dtype=np.uint8)

plt.subplot(3,3,1),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(3,3,2),plt.imshow(erosion),plt.title('Erode')
plt.xticks([]), plt.yticks([])
plt.subplot(3,3,3),plt.imshow(dilation),plt.title('Dilation')
plt.xticks([]), plt.yticks([])
plt.subplot(3,3,4),plt.imshow(opening),plt.title('Opening')
plt.xticks([]), plt.yticks([])
plt.subplot(3,3,5),plt.imshow(closing),plt.title('Closing')
plt.xticks([]), plt.yticks([])
plt.subplot(3,3,6),plt.imshow(closing_scratches),plt.title('Closing_Scratches')
plt.xticks([]), plt.yticks([])
plt.subplot(3,3,7),plt.imshow(gradient),plt.title('Gradient')
plt.xticks([]), plt.yticks([])
plt.subplot(3,3,8),plt.imshow(tophat),plt.title('Top Hat')
plt.xticks([]), plt.yticks([])
plt.subplot(3,3,9),plt.imshow(blackhat),plt.title('Black Hat')
plt.xticks([]), plt.yticks([])
plt.show()

