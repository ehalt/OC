import cv2


img = cv2.imread("baby.jpg")

imgCanny = cv2.Canny(img,50,70)

cv2.imshow("Canny image", imgCanny)

cv2.waitKey(0)