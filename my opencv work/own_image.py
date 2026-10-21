import cv2
import numpy as np 

img = np.zeros((500,500))

img2 = np.ones((600, 600))

# img3 = np.full((200, 200), 200)

cv2.imshow("zerosssssss", img)

cv2.imshow("onesssssssss", img2)
# cv2.imshow("filllllllll", img3)

cv2.waitKey(0)