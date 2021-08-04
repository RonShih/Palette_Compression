## Target
This program implements image compression in color lookup table (also called palette) in python.  
Assume the sender will transmit both image and color lookup table to the receiver, we can compress the image by using the index of color-lookup table to alternate RGB values. Note that the output in this program is a single channel gray-level image.

## Steps of DCT compression: 
1. Build a color-lookup table with 256 entries by dividing R(0-255), G(0-255), B(0-255) space.  
2. Alternate RGB value by table index
3. (optional) Derive its PSNR(Peak signal-to-noise ratio) value.


## 調色盤壓縮流程：
1. 以大(H)中(M)小(L)的排列組合來建立256色的color lookup table
2. 以index來取代原圖的RGB值
3. 計算其PSNR值

PSNR:
將original image和 output image帶入公式計算即可得出PSNR
