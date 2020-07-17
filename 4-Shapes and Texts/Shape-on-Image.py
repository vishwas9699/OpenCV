import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# print(img)
# img[:]= 255,0,0 # blue

cv2.line(img,(0,0),(512,512),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)
cv2.circle(img,(400,50),30,(255,255,0),5)

cv2.imshow("Output",img)
cv2.waitKey(0)