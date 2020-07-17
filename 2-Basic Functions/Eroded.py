import cv2
import numpy as np

img= cv2.imread("Resources\Test Image.jpg")
Kernal = np.ones((5,5),np.uint8)

imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,Kernal,iterations=1)
imgEroded = cv2.erode(imgDialation,Kernal,iterations=1)

cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dialation image",imgDialation)
cv2.imshow("Eroded image",imgEroded)
cv2.waitKey(0)