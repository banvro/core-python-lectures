import cv2

img = cv2.imread("image.png")

# print(img)
# to crop
# img[y1 : y2, x1 : x2]
print(img.shape)

new_img = img[100 : 900, 500 : 1200]

cv2.imshow("Orginal", img)
cv2.imshow("New Croped Image", new_img)

cv2.waitKey(0)