import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while 1:

    # Take each frame
    _, frame = cap.read()
    frame = cv2.medianBlur(frame, 5)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cimg = cv2.cvtColor(frame_gray, cv2.COLOR_GRAY2BGR)

    circles = cv2.HoughCircles(frame_gray, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=100, param2=30, minRadius=10, maxRadius=50)

    try:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # draw the outer circle
            cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
    except:
        continue

    cv2.imshow('detected circles', cimg)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
