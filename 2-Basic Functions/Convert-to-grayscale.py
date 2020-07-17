import cv2

img= cv2.imread("Resources\Test Image.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Grayimage",imgGray)
cv2.waitKey(0)