import cv2

cap = cv2.VideoCapture(0)

while True:
    r, f = cap.read()
    
    gray_video = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    hsv_video = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
    
    cv2.imshow("orignal video", f)
    cv2.imshow("Gray video", gray_video)
    cv2.imshow("hsv_video video", hsv_video)
    
    if cv2.waitKey(1) & 0xff == ord("q"):
        break