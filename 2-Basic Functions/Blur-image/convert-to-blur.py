import cv2

img= cv2.imread("2-Basic Functions\Blur-image\Image.jpg")

imgBlur = cv2.GaussianBlur(img,(9,9),0)

cv2.imshow("Blur Image",imgBlur)
cv2.waitKey(0)