import cv2

def empty(a):
    pass


path = "Resources\lambo.png"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Minimum","TrackBars",0,179,empty)
cv2.createTrackbar("Hue Maximum","TrackBars",179,179,empty)
cv2.createTrackbar("Saturation Minimum","TrackBars",0,255,empty)
cv2.createTrackbar("Saturation Maximum","TrackBars",255,255,empty)
cv2.createTrackbar("Value Minimum","TrackBars",0,255,empty)
cv2.createTrackbar("Value Maximum","TrackBars",255,255,empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Minimum","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Maximum","TrackBars")
    s_min = cv2.getTrackbarPos("Saturation Minimum","TrackBars")
    s_max = cv2.getTrackbarPos("Saturation Maximum","TrackBars")
    v_min = cv2.getTrackbarPos("Value Minimum","TrackBars")
    v_max = cv2.getTrackbarPos("Value Maximum","TrackBars")


    cv2.imshow("Original Image",img)
    cv2.imshow("HSV Image",imgHSV)
    cv2.waitKey(1)