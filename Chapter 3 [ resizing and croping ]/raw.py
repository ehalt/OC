import cv2
import numpy as np

img = cv2.imread("baby.jpg")
print(img.shape)
# resizing

imgResize = cv2.resize(img, (300, 200))
# crop image
imgCropped = img[0:200, 200:500]


cv2.imshow("Image", img)
cv2.imshow("Image That resized", imgResize)
cv2.imshow("Cropped image", imgCropped)


cv2.waitKey(0)




