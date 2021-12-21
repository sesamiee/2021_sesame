import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('./xml/face.xml')

if not cap.isOpened():
    print("camera open failed")
    exit()

while True :
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h),(255,0,0),2) #넣을 사진, 시작좌표 , 끝좌표, 색깔, 두께
    if not ret :
        break

    cv2.imshow("output",frame)

    #out.write(frame)
    #1000 -> 1초
    if cv2.waitKey(1) == 13:
        break
        

cap.release()
cv2.destroyALLWindows()
