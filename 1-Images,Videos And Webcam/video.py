import cv2

cap = cv2.VideoCapture("Resources\Test Video.mp4") # cv2.VideoCapture() for reading video file
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'): # for delay
         break