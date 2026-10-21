import cv2

img = cv2.imread("image.png") # RGB

# opencv always read images in  ---> BGR 

# 1) ndim ----> dimmension of your image 
print(img.ndim)

# 2) shape -----
print(img.shape)

# 2) size --> total 
print(img.size)

# dtype 
print(img.dtype)


cv2.imshow("Girl Image", img)

cv2.waitKey(0)