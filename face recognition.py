import cv2

# create cascade classifier object
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# reading img
img = cv2.imread(r"C:\Users\hp\PycharmProjects\opencv\face1.jpg")
img2 = cv2.imread(r"C:\Users\hp\PycharmProjects\opencv\f5.jpg")

# converting coloured img to grayscale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# search the coordinates of the face
faces = face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)
faces2 = face_cascade.detectMultiScale(gray_img2,scaleFactor=1.05,minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)
    img2 = cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 3)

# resizing the img in order to display img properly
#resized_img = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))

cv2.imshow("GRAY", img)
cv2.imshow("GRAY", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


