import cv2
import numpy as np

img = cv2.imread("Resources\lambo.png")
print(img.shape)

imgCropped=img[0:200,200:500]
print(imgCropped.shape)

cv2.imshow("Output",img)
cv2.imshow("Cropped Output",imgCropped)
cv2.waitKey(0)