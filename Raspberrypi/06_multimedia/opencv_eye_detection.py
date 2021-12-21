import cv2

# xml 필터 파일 로드
face_cascade = cv2.CascadeClassifier('./xml/face.xml')
eye_cascade = cv2.CascadeClassifier('./xml/eye.xml')

img = cv2.imread('avengers.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray)

for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h),(255,0,0),2) #넣을 사진, 시작좌표 , 끝좌표, 색깔, 두께

    # 눈 식별(ROI(Region of Interest),관심영역)
    roi_color = img[y:y+h, x:x+w]
    roi_gray = gray[y:y+h, x:x+w]

eyes = eye_cascade.detectMultiScale(roi_gray)
for(ex,ey,ew,eh) in faces:
    cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh),(0,255,0),2) #넣을 사진, 시작좌표 , 끝좌표, 색깔, 두께


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
