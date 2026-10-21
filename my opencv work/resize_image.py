import cv2

img = cv2.imread("image.png")

resied_img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)
# new = cv2.resize(img, (0, 0), fx = 0.2, fy = 0.2)
# new1 = cv2.resize(img, (0, 0), fx = 0.2, fy = 0.8)
# new_img = cv2.resize(img, (1000, 1400))

cv2.imwrite("new.png", resied_img)

cv2.imshow("Orginal", img)
cv2.imshow("Resiedd image", resied_img)
# cv2.imshow("20%", new)
# cv2.imshow("radom", new1)

# cv2.imshow("resizeeee", new_img)

cv2.waitKey(0)