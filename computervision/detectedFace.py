import cv2

# img = cv2.imread('python1.jpeg')
import cv2

# img = cv2.imread('python1.jpeg')

# print(img)

# cv2.imshow('my window',img)

# cv2.waitKey(10000)

cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier('haarcascade.xml')

while True:
     
    # reading a single frame from capture point
    ret, frame = cap.read()

    faces = classifier.detectMultiScale(frame)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 0, 200), 3)

    # displaying the frames in a window
    cv2.imshow('my webcam', frame)

    # for quiting the window on k
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()        


