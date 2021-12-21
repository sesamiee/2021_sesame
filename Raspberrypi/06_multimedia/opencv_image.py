import cv2

img = cv2.imread('jed.jpg')
img2 = cv2.resize(img, (1000,800))
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#edge선 추출
edge1 = cv2.canny(img, 50, 100)
edge2 = cv2.canny(img, 100, 150)
edge3 = cv2.canny(img, 150, 200)

#cv2.imshow('jed',img)
#cv2.imshow('jed2',img2)
#cv2.imshow('jed3',img3)
cv2.imshow('edge1',edge1)
cv2.imshow('edge2',edge2)
cv2.imshow('edge3',edge3)

#ENTER : 13, ESC = 27
while True :
    if cv2.waitKey() ==  13:
        break

#파일 저장하기 
cv2.imwrite('jed_GREY.jpg',img3)


cv2.destroyAllWindows()
