import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    isTrue, frame = cap.read()

    if isTrue:
        height, width, _ = frame.shape

        hsv = cv.cvtColor (frame, cv.COLOR_BGR2HSV)

        #dikey çizgiler
        cv.line (frame, (width // 3, 0), (width // 3, height), (0, 255, 0), 2)
        cv.line (frame, (2 * width // 3, 0), (2 * width // 3, height), (0, 255, 0), 2)

        #yatay çizgiler
        cv.line (frame, (0, height // 3), (width, height // 3), (0, 255, 0), 2)
        cv.line (frame, (0, 2 * height // 3), (width, 2 * height // 3), (0, 255, 0), 2)

        #yeşil mask
        lower_green = (35, 80, 80)
        upper_green = (85, 255, 255)

        mask = cv.inRange (hsv, lower_green, upper_green)
        #cv.imshow ("Mask", mask)

        #kontur bulma ve kordinat tespiti
        contours, hierarchy = cv.findContours (mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        message = "Kare Aranıyor"

        if contours: 
            largest_contour = max (contours, key = cv.contourArea)

            area = cv.contourArea (largest_contour)

            if area > 500:
                M = cv.moments (largest_contour)

                if M ["m00"] != 0:
                    cx = int (M["m10"] / M["m00"])
                    cy = int (M["m01"] / M["m00"])

                x,y,w,h = cv.boundingRect (largest_contour)
                cv.rectangle (frame, (x,y), (x + w, y + h), (0, 0, 255), 2)

                cv.putText (frame, f"Center: ({cx}, {cy})", (cx + 10, cy - 10), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2)

                #hücre belirleme
                col = min(cx * 3 // width, 2)
                row = min(cy * 3 // height, 2)

                cell_no = row * 3 + col + 1

                message = f"Hücre: {cell_no}"

        cv.putText (frame, message, (20, 40), cv.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 2)

        cv.imshow('video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break

    else:
        break

cap.release()
cv.destroyAllWindows()