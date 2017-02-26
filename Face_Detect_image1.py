
import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 5, 5)


for f in faces:
    x, y, w, h = [ v for v in f ]
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))

    sub_face = img[y:y+h, x:x+w]
    resize = cv2.resize(sub_face,(224,224))
    cv2.imwrite("", resize)

cv2.imshow("", sub_face)

#cv2.imwrite('', img)
#cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()