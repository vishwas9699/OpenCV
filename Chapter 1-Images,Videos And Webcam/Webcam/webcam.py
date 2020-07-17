import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640) #id=3 for setting width
cap.set(4,480) #id=4 for setting height
cap.set(10,100) # id=10 for setting Brightness
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
         break