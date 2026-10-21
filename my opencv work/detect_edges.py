import cv2


img = cv2.imread("new.png")
g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

e_img = cv2.Canny(g_img, 200, 200)

cv2.imwrite("edges.png", e_img)

cv2.imshow("origknla", img)
cv2.imshow("edges", e_img)

cv2.waitKey(0)