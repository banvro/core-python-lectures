import cv2

# 0 - camera

cap = cv2.VideoCapture(0)   

while True:
    ret, frame = cap.read()
    # 1 --> for horizential flip 
    # 0 ---> Vertical flip
    # -1 ---> for both
    frame1 = cv2.flip(frame, 1)
    
    cv2.putText(frame1, "Hello World", (100, 80), cv2.FONT_HERSHEY_DUPLEX, 2, (9, 201, 2), 3)
    
    cv2.imshow("My Web Cam", frame1)
    
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

