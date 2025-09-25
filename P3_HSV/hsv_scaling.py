#import required libraries
import cv2
import numpy as np

# setting up callback functions for trackbars
def onTrack1(val):
    global hueLow
    hueLow = val

def onTrack2(val):
    global hueHigh
    hueHigh = val

def onTrack3(val):
    global satLow
    satLow = val

def onTrack4(val):
    global satHigh
    satHigh = val

def onTrack5(val):
    global valLow
    valLow = val

def onTrack6(val):
    global valHigh
    valHigh = val


# Trackbar window
cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars', 400, 300)

# initial values of trackbar slider
hueLow, hueHigh = 0, 179
satLow, satHigh = 0, 255
valLow, valHigh = 0, 255

# creating trackbars
cv2.createTrackbar('Hue Low', 'Trackbars', 0, 179, onTrack1)
cv2.createTrackbar('Hue High', 'Trackbars', 179, 179, onTrack2)
cv2.createTrackbar('Sat Low', 'Trackbars', 0, 255, onTrack3)
cv2.createTrackbar('Sat High', 'Trackbars', 255, 255, onTrack4)
cv2.createTrackbar('Val Low', 'Trackbars', 0, 255, onTrack5)
cv2.createTrackbar('Val High', 'Trackbars', 255, 255, onTrack6)

# Input Image
image = cv2.imread('./images/balls.jpg')

while True:
    frameHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # lower and upper boundaries for color range in HSV
    lowerBound = np.array([hueLow, satLow, valLow])
    upperBound = np.array([hueHigh, satHigh, valHigh])

    mask = cv2.inRange(frameHSV, lowerBound, upperBound) # Creating Mask
    masked = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow('mask', mask)
    cv2.imshow('Ball', image)
    cv2.imshow('masked', masked)

    print("Lower Bound: ", lowerBound)
    print("Upper Bound: ", upperBound)

    if cv2.waitKey(1) & 0xFF == ord('q'): # to quit the window press "q"
        break

cv2.destroyAllWindows()
