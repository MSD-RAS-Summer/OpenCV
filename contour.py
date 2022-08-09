import numpy as np
import cv2
import imutils
import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--input", type=str)
parser.add_argument("--min", type=int)
parser.add_argument("--max", type=int)
parser.add_argument("--thickness", type=int)
options = parser.parse_args()

if options.input:
    print("input: {}".format(options.input))
    I = options.input
else:
    print("NO INPUT IMAGE GIVEN")

if options.min:
    print("min: {}".format(options.min))
    MIN = options.min
else:
    MIN = 220

if options.max:
    print("max: {}".format(options.max))
    MAX = options.max
else:
    MAX = 240

if options.thickness:
    print("thickness: {}".format(options.thickness))
    THICKNESS = options.thickness
else:
    THICKNESS = 2

if I:
    # OPENCV METHODS BELOW ---------------------------------------
    
    # load the two input images
    img = cv2.imread(I)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, MIN, MAX, cv2.THRESH_BINARY_INV)[1]
    
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)
    
    output = img.copy()
    cv2.drawContours(output, [c], -1, (0, 255, 0), THICKNESS)
    (x, y, w, h) = cv2.boundingRect(c)
    
    head,tail = os.path.split(I)
    cv2.imwrite(head+'Contour'+tail,output)

    # OPENCV METHODS ABOVE ---------------------------------------