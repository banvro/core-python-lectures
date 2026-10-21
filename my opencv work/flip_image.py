import cv2

img = cv2.imread("new.png")
h_flip = cv2.flip(img, 1)
v_flip = cv2.flip(img, 0)
b_flip = cv2.flip(img, -1)

cv2.imshow("Orginal", img)
cv2.imshow("Horizantal fip", h_flip)
cv2.imshow("Veritabl fip", v_flip)
cv2.imshow("both", b_flip)

cv2.waitKey(0)