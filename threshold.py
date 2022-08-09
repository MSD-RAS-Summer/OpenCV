import numpy as np
import cv2
import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--input", type=str)
parser.add_argument("--kernel", type=int)
parser.add_argument("--constant", type=int)
options = parser.parse_args()

if options.input:
    print("input: {}".format(options.input))
    I = options.input
else:
    print("NO INPUT IMAGE GIVEN")

if options.kernel:
    print("kernel: {}".format(options.kernel))
    kernel = options.kernel
else:
    kernel = 11

if options.constant:
    print("constant: {}".format(options.constant))
    constant = options.constant
else:
    constant = 4

if I:
    # OPENCV METHODS BELOW ---------------------------------------
    
    # load the two input images
    img = cv2.imread(I)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    thresh = cv2.adaptiveThreshold(gray , 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , kernel , constant)
    
    head,tail = os.path.split(I)
    cv2.imwrite(head+'Threshold'+tail,thresh)

    # OPENCV METHODS ABOVE ---------------------------------------