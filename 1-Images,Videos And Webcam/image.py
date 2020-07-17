import cv2
print("Images")

img = cv2.imread("Resources\Test Image.jpg") # cv2.imread for reading images

cv2.imshow("Output",img) # cv2.imshow for outputing the data
cv2.waitKey(0) # delay
