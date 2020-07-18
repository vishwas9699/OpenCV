import cv2

path = "Resources\lambo.png"

img = cv2.imread(path)
ImgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("Original Output",img)
cv2.imshow("HSV Output",ImgHSV)

cv2.waitKey(0)