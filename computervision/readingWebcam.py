import cv2

# img = cv2.imread('python1.jpeg')

# print(img)

# cv2.imshow('my window',img)

# cv2.waitKey(10000)

cap = cv2.VideoCapture(0)

while True:
     
    # reading a single frame from capture point
    ret, frame = cap.read()

    # displaying the frames in a window
    cv2.imshow('my webcam', frame)

    # for quiting the window on k
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindow()
cap.release()        