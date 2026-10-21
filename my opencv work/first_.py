import cv2

# help to read images 

img = cv2.imread("image.png")

cv2.imshow("Nature Image", img)

cv2.waitKey(0)