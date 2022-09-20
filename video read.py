import cv2
cap=cv2.VideoCapture('http://192.168.0.100:8080/video')

while True:
    ret,frame = cap.read()
    
    if ret == False:
        continue
    
    cv2.imshow("video frame",frame)
  
    key_pressed = cv2.waitKey(1) & 0xFF
    
    if key_pressed == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    