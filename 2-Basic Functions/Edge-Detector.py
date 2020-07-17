import cv2

img= cv2.imread("Resources\Test Image.jpg")

imgCanny = cv2.Canny(img,100,100)

cv2.imshow("Canny image",imgCanny)
cv2.waitKey(0)