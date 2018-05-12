import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Take each frame of the video
# Convert from BGR to HSV color-space
# We threshold the HSV image for a range of blue color
# Now extract the blue object alone, we can do whatever on that image we want.

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    YCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)

    HSV_lower = np.array([61, 70, 31])
    HSV_upper = np.array([95, 235, 168])
    YCbCr_lower = np.array([0, 0, 0])
    YcbCr_upper = np.array([255, 255, 255])
    RGB_lower = np.array([0, 0, 0])
    RGB_upper = np.array([255, 255, 255])

    # Threshold the image to get specific colors
    mask_HSV = cv2.inRange(hsv, HSV_lower, HSV_upper)
    mask_YCbCr = cv2.inRange(YCrCb, YCbCr_lower, YcbCr_upper)
    mask_RGB = cv2.inRange(frame, RGB_lower, RGB_upper)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask_HSV)
    res = cv2.bitwise_and(frame, res, mask=mask_YCbCr)
    res = cv2.bitwise_and(frame, res, mask=mask_RGB)

    kernel = np.ones((8, 8), np.uint8)
    opening = cv2.morphologyEx(res, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('frame', frame)
    cv2.imshow('res', res)
    cv2.imshow('opening', closing)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()