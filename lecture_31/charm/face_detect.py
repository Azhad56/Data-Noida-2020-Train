import cv2
import time


cap = cv2.VideoCapture(0)

classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    retval, image = cap.read()

    if retval:

        faces = classifier.detectMultiScale(image)

        for face in faces:
            x, y, w, h = face

            cv2.rectangle(img=image, pt1=(x, y), pt2=(x+w, y+h), color=(0, 255, 0), thickness=10)

        cv2.imshow("whole", image)

    key = cv2.waitKey(10)

    if key == ord("q"):
        break
    if key == ord("c"):
        cv2.imwrite("classroom.png", image)


cap.release()
cv2.destroyAllWindows()