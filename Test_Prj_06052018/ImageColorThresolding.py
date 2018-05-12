import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Take each frame of the video
# Convert from BGR to HSV color-space
# We threshold the HSV image for a range of blue color
# Now extract the blue object alone, we can do whatever on that image we want.


def create_track_bar():
    # Create a black image, a window
    cv2.namedWindow('Threshold', cv2.WINDOW_NORMAL)

    # create trackbars for color change
    cv2.createTrackbar('H_Max', 'Threshold', 0, 255, get_track_bar_pos)
    cv2.createTrackbar('H_Min', 'Threshold', 0, 255, get_track_bar_pos)
    cv2.createTrackbar('S_Max', 'Threshold', 0, 255, get_track_bar_pos)
    cv2.createTrackbar('S_Min', 'Threshold', 0, 255, get_track_bar_pos)
    cv2.createTrackbar('V_Max', 'Threshold', 0, 255, get_track_bar_pos)
    cv2.createTrackbar('V_Min', 'Threshold', 0, 255, get_track_bar_pos)

    cv2.createTrackbar('Y_Max', 'Threshold', 0, 255, get_track_bar_pos)
    cv2.createTrackbar('Y_Min', 'Threshold', 0, 255, get_track_bar_pos)
    cv2.createTrackbar('Cb_Max', 'Threshold', 0, 255, get_track_bar_pos)
    cv2.createTrackbar('Cb_Min', 'Threshold', 0, 255, get_track_bar_pos)
    cv2.createTrackbar('Cr_Max', 'Threshold', 0, 255, get_track_bar_pos)
    cv2.createTrackbar('Cr_Min', 'Threshold', 0, 255, get_track_bar_pos)

    cv2.createTrackbar('R_Max', 'Threshold', 0, 255, get_track_bar_pos)
    cv2.createTrackbar('R_Min', 'Threshold', 0, 255, get_track_bar_pos)
    cv2.createTrackbar('G_Max', 'Threshold', 0, 255, get_track_bar_pos)
    cv2.createTrackbar('G_Min', 'Threshold', 0, 255, get_track_bar_pos)
    cv2.createTrackbar('B_Max', 'Threshold', 0, 255, get_track_bar_pos)
    cv2.createTrackbar('B_Min', 'Threshold', 0, 255, get_track_bar_pos)

    cv2.setTrackbarPos('H_Max', 'Threshold', 255)
    cv2.setTrackbarPos('H_Min', 'Threshold', 0)
    cv2.setTrackbarPos('S_Max', 'Threshold', 255)
    cv2.setTrackbarPos('S_Min', 'Threshold', 0)
    cv2.setTrackbarPos('V_Max', 'Threshold', 255)
    cv2.setTrackbarPos('V_Min', 'Threshold', 0)

    cv2.setTrackbarPos('Y_Max', 'Threshold', 255)
    cv2.setTrackbarPos('Y_Min', 'Threshold', 0)
    cv2.setTrackbarPos('Cb_Max', 'Threshold', 255)
    cv2.setTrackbarPos('Cb_Min', 'Threshold', 0)
    cv2.setTrackbarPos('Cr_Max', 'Threshold', 255)
    cv2.setTrackbarPos('Cr_Min', 'Threshold', 0)

    cv2.setTrackbarPos('R_Max', 'Threshold', 255)
    cv2.setTrackbarPos('R_Min', 'Threshold', 0)
    cv2.setTrackbarPos('G_Max', 'Threshold', 255)
    cv2.setTrackbarPos('G_Min', 'Threshold', 0)
    cv2.setTrackbarPos('B_Max', 'Threshold', 255)
    cv2.setTrackbarPos('B_Min', 'Threshold', 0)


def get_track_bar_pos(self):
    H_Max = cv2.getTrackbarPos('H_Max', 'Threshold')
    H_Min = cv2.getTrackbarPos('H_Min', 'Threshold')
    S_Max = cv2.getTrackbarPos('S_Max', 'Threshold')
    S_Min = cv2.getTrackbarPos('S_Min', 'Threshold')
    V_Max = cv2.getTrackbarPos('V_Max', 'Threshold')
    V_Min = cv2.getTrackbarPos('V_Min', 'Threshold')

    Y_Max = cv2.getTrackbarPos('Y_Max', 'Threshold')
    Y_Min = cv2.getTrackbarPos('Y_Min', 'Threshold')
    Cb_Max = cv2.getTrackbarPos('Cb_Max', 'Threshold')
    Cb_Min = cv2.getTrackbarPos('Cb_Min', 'Threshold')
    Cr_Max = cv2.getTrackbarPos('Cr_Max', 'Threshold')
    Cr_Min = cv2.getTrackbarPos('Cr_Min', 'Threshold')

    R_Max = cv2.getTrackbarPos('R_Max', 'Threshold')
    R_Min = cv2.getTrackbarPos('R_Min', 'Threshold')
    G_Max = cv2.getTrackbarPos('G_Max', 'Threshold')
    G_Min = cv2.getTrackbarPos('G_Min', 'Threshold')
    B_Max = cv2.getTrackbarPos('B_Max', 'Threshold')
    B_Min = cv2.getTrackbarPos('B_Min', 'Threshold')

    global HSV_lower
    global HSV_upper
    global YcbCr_upper
    global YCbCr_lower
    global RGB_upper
    global RGB_lower
    HSV_upper = np.array([H_Max, S_Max, V_Max])
    HSV_lower = np.array([H_Min, S_Min, V_Min])
    YcbCr_upper = np.array([Y_Max, Cb_Max, Cr_Max])
    YCbCr_lower = np.array([Y_Min, Cb_Min, Cr_Min])
    RGB_upper = np.array([R_Max, G_Max, B_Max])
    RGB_lower = np.array([R_Min, G_Min, B_Min])


HSV_upper = np.array([255, 255, 255])
RGB_upper = np.array([255, 255, 255])
YcbCr_upper = np.array([255, 255, 255])
HSV_lower = np.array([0, 0, 0])
RGB_lower = np.array([0, 0, 0])
YCbCr_lower = np.array([0, 0, 0])
create_track_bar()

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    YCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)

    # Threshold the image to get specific colors
    mask_HSV = cv2.inRange(hsv, HSV_lower, HSV_upper)
    mask_YCbCr = cv2.inRange(YCrCb, YCbCr_lower, YcbCr_upper)
    mask_RGB = cv2.inRange(YCrCb, RGB_lower, RGB_upper)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask_HSV)
    res = cv2.bitwise_and(frame, res, mask=mask_YCbCr)
    res = cv2.bitwise_and(frame, res, mask=mask_RGB)

    cv2.imshow('frame', frame)
    cv2.imshow('mask HSV', mask_HSV)
    cv2.imshow('mask YcbCr', mask_YCbCr)
    cv2.imshow('mask RGB', mask_RGB)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
