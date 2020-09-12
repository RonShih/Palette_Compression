# Palette_Compression
流程:
1. 以大(H)中(M)小(L)的排列組合來建立256色的color lookup table
2. 以index來取代原圖的RGB值
3. 計算其 PSNR 值

PSNR:
將original image和 output image帶入公式計算即可得出PSNR
