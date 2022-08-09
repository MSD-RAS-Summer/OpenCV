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
    src = cv2.imread(I)
    cropped_image = src[src.shape[0]/2-options.width/2:src.shape[0]/2+options.width/2,src.shape[1]/2-options.width/2:src.shape[1]/2+options.width/2]
    
    head,tail = os.path.split(I)
    cv2.imwrite(head+'Cropped'+tail,cropped_image)

    # OPENCV METHODS ABOVE ---------------------------------------