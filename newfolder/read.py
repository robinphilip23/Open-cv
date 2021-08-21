import cv2 as cv

def rescaleframe(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# To read a video
capture = cv.VideoCapture('Videos/Rick Astley - Never Gonna Give You Up (Official Music Video).webm')

convert_grey = cv.cvtColor(capture, cv.COLOR_BGR2GRAY)
cv.imshow('Grey Rick', convert_grey)

while True:
    cascade = cv.Canny(convert_grey,125,175)
    cv.imshow('Canny', cascade)
    isTrue, frame  = cascade.read()
    frame_resize = rescaleframe(frame,scale=0.2)
    cv.imshow('Video', frame)
    cv.imshow('Resized video', frame_resize)    

    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
capture.destroyAllWindows()