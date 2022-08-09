import numpy as np
import cv2
import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--input", type=str)
parser.add_argument("--width", type=int)
parser.add_argument("--height", type=int)
options = parser.parse_args()

if options.input:
    print("input: {}".format(options.input))
    I = options.input
else:
    print("NO INPUT IMAGE GIVEN")

if I:
    # OPENCV METHODS BELOW ---------------------------------------
    
    # load the two input images
    img = cv2.imread(I)
    # convert the images to grayscale
    img = cv2.resize(img, (options.width,options.height), interpolation = cv2.INTER_AREA)
    
    head,tail = os.path.split(I)
    cv2.imwrite(head + 'Resized' + tail,img)

    # OPENCV METHODS ABOVE ---------------------------------------