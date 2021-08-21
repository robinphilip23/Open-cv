import cv2 as cv

image = cv.imread('Photos/rick.jpg')
cv.imshow('Rick',image)
# Converting a image to Greyscale

convert_grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Grey Rick', convert_grey)

#Blur
"""
blur  = cv.GaussianBlur(image,(7,7), cv.BORDER_DEFAULT)
cv.imshow('Blurred image', blur)
"""

# Edge Cascade
cascade = cv.Canny(convert_grey,125,175)
cv.imshow('Canny', cascade)


# Dialating the image

dilated = cv.dilate(cascade, (7,7), iterations=3)
cv.imshow('Dilated image', dilated)

# Eroded image
eroded = cv.erode(dilated,(7,7), iterations=3)
cv.imshow('Eroded',eroded)

# Resize 
resized = cv.resize(image,(500,500),interpolation=cv.INTER_CUBIC
)

cv.imshow('Resized',resized)

# Cropping 
cropped = image[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)