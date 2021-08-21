import cv2 as cv
# reading images
image = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', image)
cv.waitKey(0) 
