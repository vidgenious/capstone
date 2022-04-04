import cv2 as cv
import numpy as np

THRESHOLD = 0.7

image = cv.imread("fullimage.jpg")
template = cv.imread("template2.jpg")
imageGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
templateGray = cv.cvtColor(template, cv.COLOR_BGR2GRAY)

# This results in a plot that compares the similarity
matchPlot = cv.matchTemplate(imageGray, templateGray, cv.TM_CCOEFF_NORMED)

(minVal, maxVal, minLoc, maxLoc) = cv.minMaxLoc(matchPlot)

if maxVal < THRESHOLD:

    # run pause command
    print("Pause")
else:
    # continue
    print("Continue")