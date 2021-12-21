import cv2

cap = cv2.VideoCapture('output.avi')

if not cap.isOpened():
    print("camera open failed")
    exit()

#DIVX(avi), MP4V(mp4), X264(h264)
fourcc = cv2.VideoWriter_fourcc(*'DIVX') # ('D','I','V','X')

#out = cv2.VideoWriter('output.avi', fourcc, 30, (640,480))

#카메라 사진찍기

#ret, frame = cap.read()
#cv2.imshow('frame',frame)
#cv2.imwrite('output.jpg',frame)

#동영상 촬영
while True :
    ret, frame = cap.read()
    if not ret :
        break

    cv2.imshow("frame",frame)
    #out.write(frame)
    #1000 -> 1초
    if cv2.waitKey(1) == 13:
        break
        


#out.release()
cap.release()
cv2.destroyALLWindows()