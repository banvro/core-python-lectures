import cv2

img = cv2.imread("new.png")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
new1 = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
new2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("orignal", img)
cv2.imshow("Gray", gray_img)
cv2.imshow("HLS", new1)
cv2.imshow("HSV", new2)

cv2.waitKey(0)