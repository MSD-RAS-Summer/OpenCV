import numpy as np
import cv2
import os
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--input", type=str)
options = parser.parse_args()

if options.input:
    print("input: {}".format(options.input))
    I = options.input
else:
    print("NO INPUT IMAGE GIVEN")

if I:
    # OPENCV METHODS BELOW ---------------------------------------
    
    # load the two input images
    src = cv2.imread(I)
    image = cv2.rotate(src, cv2.cv2.ROTATE_90_CLOCKWISE)
    
    head,tail = os.path.split(I)
    cv2.imwrite(head +'Rotated'+tail,image)

    # OPENCV METHODS ABOVE ---------------------------------------