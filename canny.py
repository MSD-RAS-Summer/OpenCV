import numpy as np
import cv2
import imutils
import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--input", type=str)
parser.add_argument("--blur", type=int)
parser.add_argument("--aperture", type=int)
options = parser.parse_args()

if options.input:
    print("input: {}".format(options.input))
    I = options.input
else:
    print("NO INPUT IMAGE GIVEN")

if options.blur:
    print("blur: {}".format(options.blur))
    BLUR = options.blur
else:
    BLUR = 5

if options.aperture:
    print("aperture: {}".format(options.aperture))
    APERTURE = options.aperture
else:
    APERTURE = 3

if I:
    # OPENCV METHODS BELOW ---------------------------------------
    
    img = cv2.imread(I)
    height = img.shape[0]
    width = img.shape[1]
    r = float(1200)/ width
    dim = (int(width*r), int(height * r))
    
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    sigma = 0.33
    v = np.median(resized)
    #---- Apply automatic Canny edge detection using the computed median----
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (BLUR, BLUR), 0)
    dst = cv2.Canny(blurred, lower, upper, apertureSize = 3)
    
    head,tail = os.path.split(I)
    cv2.imwrite(head+'CannyEdges'+tail,dst)

    # OPENCV METHODS ABOVE ---------------------------------------