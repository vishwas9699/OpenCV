import cv2
import numpy as np

img= cv2.imread("Resources\Test Image.jpg")
Kernal = np.ones((5,5),np.uint8)

imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,Kernal,iterations=5)

cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dialation image",imgDialation)
cv2.waitKey(0)