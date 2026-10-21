import cv2

img = cv2.imread("new.png")

# new_img = cv2.rotate(img, 1) # 1 -> 180
new_img = cv2.rotate(img, 2) # 2 -> 90
# new_img = cv2.rotate(img, 3) # 2 -> 90

cv2.imshow("orgibal", img)
cv2.imshow("roteated", new_img)

cv2.waitKey(0)