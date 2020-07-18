import cv2

path = "Resources\lambo.png"
img = cv2.imread(path)


cv2.imshow("Original Output",img)
cv2.waitKey(0)