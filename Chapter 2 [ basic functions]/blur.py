import cv2



img = cv2.imread("baby.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (19,19),0)

cv2.imshow("Gray image", imgGray)

cv2.imshow("Blur image", imgBlur)


cv2.waitKey(0)