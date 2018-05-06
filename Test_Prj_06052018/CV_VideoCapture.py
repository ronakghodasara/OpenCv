import cv2

# To capture a video, you need to create a VideoCapture object.
# Its argument can be either the device index or the name of a video file.
# Device index is just the number to specify which camera.
# Normally one camera will be connected (as in my case). So I simply pass 0 (or -1).
# You can select the second camera by passing 1 and so on.
# After that, you can capture frame-by-frame.
# But at the end, do not forget to release the capture.

cap = cv2.VideoCapture(0)

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print '\nAvailable Color Spaces :'
print flags
print '\n'

# You can also access some of the features of this video using cap.get(propId) method
# where propId is a number from 0 to 18.
# Each number denotes a property of the video (if it is applicable to that video)
# Some of these values can be modified using cap.set(propId, value). Value is the new value you want.
print 'CV_CAP_PROP_POS_AVI_RATIO.{}'.format(cap.get(2))
print 'CV_CAP_PROP_FRAME_WIDTH.{}'.format(cap.get(3))
print 'CV_CAP_PROP_FRAME_HEIGHT.{}'.format(cap.get(4))

while cap.isOpened():
    # Capture frame-by-frame
    # cap.read() returns a bool (True/False).
    # If frame is read correctly, it will be True.
    # So you can check end of the video by checking this return value.
    ret, frame = cap.read()

    # Sometimes, cap may not have initialized the capture.
    # In that case, this code shows error.
    # You can check whether it is initialized or not by the method cap.isOpened().
    # If it is True, OK. Otherwise open it using cap.open().

    # Our operations on the frame come here
    GRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    HLS = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    LAB = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    LUV = cv2.cvtColor(frame, cv2.COLOR_BGR2LUV)
    XYZ = cv2.cvtColor(frame, cv2.COLOR_BGR2XYZ)
    YCrCb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
    YUV = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)

    # Display the resulting frame
    cv2.imshow('frame_GRAY', GRAY)
    cv2.imshow('frame_HLS', HLS)
    cv2.imshow('frame_HSV', HSV)
    cv2.imshow('frame_LAB', LAB)
    cv2.imshow('frame_LUV', LUV)
    cv2.imshow('frame_XYZ', XYZ)
    cv2.imshow('frame_YCrCb', YCrCb)
    cv2.imshow('frame_YUV', YUV)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
