# -*- coding: utf-8 -*-
import numpy as np
import pickle
from PIL import Image
from scipy.signal import convolve2d
import os.path
import cv2

pickledPsfFilename =os.path.join(os.path.dirname( __file__),"psf.pkl")

with open(pickledPsfFilename, 'rb') as pklfile:
    psfDictionary = pickle.load(pklfile, encoding='latin1')


# def PsfBlur(img, psfid):
#     imgarray = np.array(img, dtype="float32")
#     kernel = psfDictionary[psfid]
#     convolved = convolve2d(imgarray, kernel, mode='same', fillvalue=255.0).astype("uint8")
#     img = Image.fromarray(convolved)
#     return img

def PsfBlur(img, psfid):
    kernel = psfDictionary[psfid]
    convolved = cv2.filter2D(img, -1, kernel)
    return convolved
    
def PsfBlur_random(img):
    psfid = np.random.randint(0, len(psfDictionary))
    return PsfBlur(img, psfid)
    
    
