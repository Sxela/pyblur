import numpy as np
from PIL import Image
from scipy.signal import convolve2d
import cv2

# boxKernelDims = [3,5,7,9]

# def BoxBlur_random(img):
#     kernelidx = np.random.randint(0, len(boxKernelDims))    
#     kerneldim = boxKernelDims[kernelidx]
#     return BoxBlur(img, kerneldim)

# def BoxBlur(img, dim):
#     imgarray = np.array(img, dtype="float32")
#     kernel = BoxKernel(dim)
#     convolved = cv2.filter2D(imgarray, -1, kernel)
#     # convolved = convolve2d(imgarray, kernel, mode='same', fillvalue=255.0).astype("uint8")
#     # img = Image.fromarray(convolved)
#     return convolved

# def BoxKernel(dim):
#     kernelwidth = dim
#     kernel = np.ones((kernelwidth, kernelwidth), dtype=np.float32)        
#     normalizationFactor = np.count_nonzero(kernel)
#     kernel = kernel / normalizationFactor
#     return kernel

boxKernelDims = [5,7,9,12,15]

def BoxBlur_random(img):
    kernelidx = np.random.randint(0, len(boxKernelDims))    
    kerneldim = boxKernelDims[kernelidx]
    return BoxBlur(img, kerneldim)

def BoxBlur(img, dim):
    kernel = BoxKernel(dim)
    convolved = cv2.filter2D(img, -1, kernel)
    return convolved

def BoxKernel(dim):
    kernelwidth = dim
    kernel = np.ones((kernelwidth, kernelwidth), dtype=np.float32)        
    normalizationFactor = np.count_nonzero(kernel)
    kernel = kernel / normalizationFactor
    return kernel
