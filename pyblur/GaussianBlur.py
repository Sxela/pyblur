import numpy as np
from PIL import ImageFilter
import cv2

gaussianbandwidths = [0.5, 1, 1.5, 2, 2.5, 3, 3.5]

def GaussianBlur_random(img):
    gaussianidx = np.random.randint(0, len(gaussianbandwidths))
    gaussianbandwidth = gaussianbandwidths[gaussianidx]
    return GaussianBlur(img, gaussianbandwidth)

def GaussianBlur(img, bandwidth):
    img = cv2.GaussianBlur(img, (0,0), bandwidth)
    # img = img.filter(ImageFilter.GaussianBlur(bandwidth))
    return img