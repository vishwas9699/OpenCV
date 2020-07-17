import cv2

img = cv2.imread("Resources\lambo.png")
print(img.shape)

imgResize=cv2.resize(img,(300,200))
print(imgResize.shape)
cv2.imshow("Output",img)
cv2.imshow("Output.Resize",imgResize)
cv2.waitKey(0)