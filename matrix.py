from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import os

def jpeg_detector_4(userinput):
    im = Image.open(userinput).convert('L')
    #pix = im.load()
    pix = np.array(im).astype(np.float)
    r, c = pix.shape

    if r < c:
        # rotate the image
        pix = np.rot90(pix)
        r, c = pix.shape

    arr_v = np.zeros((32, 31))
    sum_v = np.zeros((c/32, r/32))

    # vertical
    for col in xrange(0, c / 32):
        for row in xrange(0, r / 32):
            for i in xrange(32):
                for j in xrange(31):
                    v1 = pix[row * 32 + i, col * 32 + j + 1]
                    v2 = pix[row * 32 + i, col * 32 + j]
                    v = v1 - v2
                    arr_v[i][j] = v

            arr_v = np.abs(arr_v)
            fft2 = np.abs(np.fft.fft2(arr_v, [32, 32]))  # FFT of vertical gradient
            if sum(fft2[0, 1:16]) == 0:
                sum2 = 0
            else:
                sum2 = (fft2[0, 4] + fft2[0, 8] + fft2[0, 12]) / sum(fft2[0, 1:16])

            sum_v[col][row] = sum2
    myarray2 = np.asarray(sum_v)
    return myarray2
userinput = "I_50.jpg"
A = jpeg_detector_4(userinput);
print A