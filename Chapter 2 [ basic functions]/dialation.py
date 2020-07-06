import cv2
import numpy as np

img = cv2.imread("baby.jpg")
# kernel here

kernel = np.ones((5,5),np.uint8)


imgCanny = cv2.Canny(img,50,70)
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dilation image", imgDilation)


cv2.waitKey(0)