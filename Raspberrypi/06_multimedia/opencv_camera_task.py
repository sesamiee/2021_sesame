import cv2

cap = cv2.VideoCapture('output.avi')

if not cap.isOpened():
    print("camera open failed")
    exit()

while True :
    ret, frame = cap.read()
    edge = cv2.canny(frame, 100, 150)
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if not ret :
        break

    cv2.imshow("output",frame)
    cv2.imshow("edge",edge)
    cv2.imshow("grey",grey)
    #out.write(frame)
    #1000 -> 1초
    if cv2.waitKey(1) == 13:
        break
        

cap.release()
cv2.destroyALLWindows()
