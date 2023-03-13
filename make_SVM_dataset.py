import cv2

webcam1 = cv2.VideoCapture(0)
# webcam2 = cv2.VideoCapture(4)
webcam2 = cv2.VideoCapture(6)

if not webcam1.isOpened():
    print("Could not open webcam1")
    exit()

if not webcam2.isOpened():
    print("Could not open webcam2")
    exit()

while webcam1.isOpened():
    status1, frame1 = webcam1.read()
    status2, frame2 = webcam2.read()

    cv2.imshow("frame1", frame1)
    cv2.imshow("frame2", frame2)

    count = int(count) + 1
    count = format(count, '08')
    
    cv2.imshow("frame1", frame1)
    cv2.imwrite("dataset/depth/" + str(count) + ".png", frame1)
    
    cv2.imshow("frame2", frame2)
    cv2.imwrite("dataset/rgb/" + str(count) + ".png", frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam1.release()
webcam2.release()
cv2.destroyAllWindows()