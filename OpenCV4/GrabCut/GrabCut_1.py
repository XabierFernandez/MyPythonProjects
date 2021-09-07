import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread('../data/Saltando.jpg')
img1 = cv.imread('../data/outer-space.jpg')

mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (50,200,575,390)
cv.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
plt.imshow(img),plt.colorbar(),plt.show()

# cv.imwrite('Saltando.jpg',img)

alpha = 0.3
beta = (1.0 - alpha)
dst = cv.addWeighted(img1, alpha, img, beta, 0.0)


cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()