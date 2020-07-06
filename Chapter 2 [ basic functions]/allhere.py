import cv2
import numpy as np


# i'm gonnna create grayscale
img = cv2.imread("baby.jpg")
# adding kernel
kernel = np.ones((5,5),np.uint8) #here uint = unsigned integer


# gray image
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# bluer image
imgBlur = cv2.GaussianBlur(imgGray,(19,19),0)
# canny image
imgCanny = cv2.Canny(img,50,70)

imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)

cv2.imshow("Gray image", imgGray)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dilation image", imgDialation)
cv2.waitKey(0)