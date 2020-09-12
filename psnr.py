import numpy as np
from cv2 import cv2

img = cv2.imread("img.bmp")
out = cv2.imread("output.bmp")
sp = img.shape

mse = 0
for i in range (sp[0]):
    for j in range (sp[1]):
        for k in range (sp[2]):
            mse += (int(img[i,j,k]) - int(out[i,j,k]))**2
mse /= sp[0]*sp[1]*sp[2]
psnr = 10*np.log10(255**2/mse)

print(psnr)
