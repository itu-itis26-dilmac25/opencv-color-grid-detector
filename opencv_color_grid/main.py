import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    isTrue, frame = cap.read()

    if isTrue:
        cv.imshow('video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break

    else:
        break

cap.release()
cv.destroyAllWindows()