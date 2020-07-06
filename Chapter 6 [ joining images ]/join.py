import cv2

import numpy as np

img = cv2.imread("baby2.jpg")

imghor = np.hstack((img,img))
imgver = np.vstack((img,img))


cv2.imshow("Horizontail", imghor)
cv2.imshow("Vertical", imgver)



cv2.waitKey(0)