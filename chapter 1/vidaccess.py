import cv2

cap = cv2.VideoCapture("sony.mp4")

while True:
    sucess, img = cap.read()
    cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'): #this line is for keyboard comand
        # when i will press 'q' key the video will be end.
        break