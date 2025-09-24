import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    cv2.imshow("Camera", frame)

    # Quit with 'q'
    if cv2.waitKey(1) & 0xFF == ord("A"):#"camera close garna ko lagi "
        break

cap.release()
cv2.destroyAllWindows()
