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

    img = cv2.imread(I)
    # convert the images to grayscale
    grayA = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    head,tail = os.path.split(I)
    cv2.imwrite(head + 'Grayscale'+ tail,grayA)

    # OPENCV METHODS ABOVE ---------------------------------------