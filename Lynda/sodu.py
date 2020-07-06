import numpy as np
import cv2

img = cv2.imread('sodu.jpg')
cv2.imshow("Original", img)

ret, thresh_basic = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
cv2.imshow("Basic Binary", thresh_basic)





cv2.waitKey(0)





