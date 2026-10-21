import cv2

img = cv2.imread("new.png")

# blr_img = cv2.blur(img, (11, 3))
blr_img = cv2.GaussianBlur(img, (11, 3), 0)

cv2.imshow("orginla", img)
cv2.imshow("blue image", blr_img)

cv2.waitKey(0)