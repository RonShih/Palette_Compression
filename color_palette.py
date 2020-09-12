import os
import numpy as np
import cv2
from os.path import getsize

def PSNR(str):
    org = cv2.imread('img.bmp')
    out = cv2.imread(str)
    sp = org.shape
    mse = 0
    for i in range (sp[0]):
        for j in range (sp[1]):
            for k in range (sp[2]):
               mse += (int(org[i,j,k]) - int(out[i,j,k]))**2
    mse /= sp[0]*sp[1]*sp[2]
    psnr = 10*np.log10(255**2/mse)
    return psnr

img = cv2.imread("img.bmp")
index_img = cv2.imread("img.bmp", 0)
output_img = img

table_b = np.array([], dtype = np.uint8)
table_g = np.array([], dtype = np.uint8)
table_r = np.array([], dtype = np.uint8)

table_b2 = np.array([], dtype = np.uint8)
table_g2 = np.array([], dtype = np.uint8)
table_r2 = np.array([], dtype = np.uint8)
#0~32
#HLL
table_b = np.arange(30,256,25)
table_g = np.zeros(10)
table_r = np.zeros(10)
#LHL
table_b2 = np.zeros(10)
table_g2 = np.arange(30,256,25)
table_r2 = np.zeros(10)
table_b = np.append(table_b, table_b2)
table_g = np.append(table_g, table_g2)
table_r = np.append(table_r, table_r2)
#LLH
table_b2 = np.zeros(10)
table_g2 = np.zeros(10)
table_r2 = np.arange(30,256,25)
table_b = np.append(table_b, table_b2)
table_g = np.append(table_g, table_g2)
table_r = np.append(table_r, table_r2)
#black & white
table_b = np.append(table_b, 0)
table_g = np.append(table_g, 0)
table_r = np.append(table_r, 0)
table_b = np.append(table_b, 255)
table_g = np.append(table_g, 255)
table_r = np.append(table_r, 255)

#31~63
#LMH
table_b2 = np.zeros(16)
table_g2 = np.arange(7,128,8)
table_r2 = np.arange(15,256,16)
table_b = np.append(table_b, table_b2)
table_g = np.append(table_g, table_g2)
table_r = np.append(table_r, table_r2)
#MLH
table_b2 = np.arange(7,128,8)
table_g2 = np.zeros(16)
table_r2 = np.arange(15,256,16)
table_b = np.append(table_b, table_b2)
table_g = np.append(table_g, table_g2)
table_r = np.append(table_r, table_r2)

#64~95
#MHL
table_b2 = np.arange(7,128,8)
table_g2 = np.arange(15,256,16)
table_r2 = np.zeros(16)
table_b = np.append(table_b, table_b2)
table_g = np.append(table_g, table_g2)
table_r = np.append(table_r, table_r2)
#LHM
table_b2 = np.zeros(16)
table_g2 = np.arange(15,256,16)
table_r2 = np.arange(7,128,8)
table_b = np.append(table_b, table_b2)
table_g = np.append(table_g, table_g2)
table_r = np.append(table_r, table_r2)

#96~127
#HML
table_b2 = np.arange(15,256,16)
table_g2 = np.arange(7,128,8)
table_r2 = np.zeros(16)
table_b = np.append(table_b, table_b2)
table_g = np.append(table_g, table_g2)
table_r = np.append(table_r, table_r2)
#HLM
table_b2 = np.arange(15,256,16)
table_g2 = np.zeros(16)
table_r2 = np.arange(7,128,8)
table_b = np.append(table_b, table_b2)
table_g = np.append(table_g, table_g2)
table_r = np.append(table_r, table_r2)

#128~159 LHH
table_b2 = np.zeros(32)
table_g2 = np.arange(7,256,8)
table_r2 = np.arange(7,256,8)
table_b = np.append(table_b, table_b2)
table_g = np.append(table_g, table_g2)
table_r = np.append(table_r, table_r2)

#160~191 HLH
table_b2 = np.arange(7,256,8)
table_g2 = np.zeros(32)
table_r2 = np.arange(7,256,8)
table_b = np.append(table_b, table_b2)
table_g = np.append(table_g, table_g2)
table_r = np.append(table_r, table_r2)

#192~223 HHL
table_b2 = np.arange(7,256,8)
table_g2 = np.arange(7,256,8)
table_r2 = np.zeros(32)
table_b = np.append(table_b, table_b2)
table_g = np.append(table_g, table_g2)
table_r = np.append(table_r, table_r2)

#224~256 HHH
table_b2 = np.arange(7,256,8)
table_g2 = np.arange(7,256,8)
table_r2 = np.arange(7,256,8)
table_b = np.append(table_b, table_b2)
table_g = np.append(table_g, table_g2)
table_r = np.append(table_r, table_r2)
lut = np.dstack((table_b, table_g, table_r))

fp = open("index.txt", "w")# 開啟檔案 "w" 複寫
sp = img.shape
diff = 30
index = 0
for i in range(sp[0]):
    for j in range(sp[1]):
        smallest = medium = biggest = img[i,j,0]
        s_clr = m_clr = b_clr = 0 #small, medium, big
        for k in range(sp[2]): #找最小值 
            if(biggest < img[i,j,k]):
                biggest = img[i,j,k]
                b_clr = k # B or G or R 為最小
            if(smallest > img[i,j,k]):
                smallest = img[i,j,k]
                s_clr = k # B or G or R 為最大
        for k in range(3):
            if(s_clr != k and b_clr != k):# 第二大
                m_clr = k
                medium = img[i,j,k]

        if((img[i,j,0] == img[i,j,1]) and (img[i,j,1] == img[i,j,2])):
            if(img[i,j,0] == 0): #(B,G,R) = (0,0,0) LLL
                index = np.unit(30)
                output_img[i,j] = lut[0][30]
            else: #(B,G,R) = (1,1,1) or (10,10,10)... HHH
                num = img[i,j,0] / 8
                index = int(num)+224
                #output_img[i,j] = index
                output_img[i,j] = lut[0][index]
            
        else:
            if(biggest - medium > diff and medium - smallest < diff): #1H 2L
                if(b_clr == 0): #HLL
                    num = img[i,j,b_clr] / 25
                    index = int(num)
                    #output_img[i,j] = lut[0][index]
                    #output_img[i,j] = index
                elif(b_clr == 1): #LHL
                    num = img[i,j,b_clr] / 25
                    index = int(num)+10
                    output_img[i,j] = lut[0][index]
                    #output_img[i,j] = index
                elif(b_clr == 2): #LLH
                    num = img[i,j,b_clr] / 25
                    index = int(num)+20
                    output_img[i,j] = lut[0][index]
                    #output_img[i,j] = index

            if(biggest - medium <= diff and medium - smallest < diff): #HHH
                num = img[i,j,0] / 8
                index = int(num)+224
                output_img[i,j] = lut[0][index]
                #output_img[i,j] = index

            #HLL LHL LLH HHL HLH LHH
            elif(biggest - medium > diff and medium - smallest >= diff):#1H 1M 1L
                if(b_clr == 2 and m_clr == 1): #LMH
                    num = img[i,j,b_clr] / 16
                    index = int(num)+32
                    output_img[i,j] = lut[0][index]
                    #output_img[i,j] = index
                elif(b_clr == 2 and m_clr == 0): #MLH
                    num = img[i,j,b_clr] / 16
                    index = int(num)+48
                    output_img[i,j] = lut[0][index]
                    #output_img[i,j] = index
                elif(b_clr == 1 and m_clr == 0): #MHL
                    num = img[i,j,b_clr] / 16
                    index = int(num)+64
                    output_img[i,j] = lut[0][index]
                    #output_img[i,j] = index
                elif(b_clr == 1 and m_clr == 2): #LHM
                    num = img[i,j,b_clr] / 16
                    index = int(num)+80
                    output_img[i,j] = lut[0][index]
                    #output_img[i,j] = index
                elif(b_clr == 0 and m_clr == 1): #HML
                    num = img[i,j,b_clr] / 16
                    index = int(num)+96
                    output_img[i,j] = lut[0][index]
                    #output_img[i,j] = index
                elif(b_clr == 0 and m_clr == 2): #HLM
                    num = img[i,j,b_clr] / 16
                    index = int(num)+112
                    output_img[i,j] = lut[0][index]    
                    #output_img[i,j] = index

            elif(biggest - medium <= diff and medium - smallest >= diff):#2H 1L
                if((b_clr == 0 and m_clr == 1) or (b_clr == 1 and m_clr == 0)): #HHL
                    num = img[i,j,b_clr] / 8
                    index = int(num)+192
                    output_img[i,j] = lut[0][index]
                    #output_img[i,j] = index
                elif((b_clr == 0 and m_clr == 2) or (b_clr == 2 and m_clr == 0)): #HLH               
                    num = img[i,j,b_clr] / 8
                    index = int(num)+160
                    output_img[i,j] = lut[0][index]
                    #output_img[i,j] = index
                elif((b_clr == 1 and m_clr == 2) or (b_clr == 2 and m_clr == 1)): #LHH
                    num = img[i,j,b_clr] / 8
                    index = int(num)+128
                    output_img[i,j] = lut[0][index]          
                    #output_img[i,j] = index
        
        fp.write(str(index) + " ") 
        index_img[i][j] = index #index
    fp.write("\n")
cv2.imwrite('index.bmp', index_img)
cv2.imwrite('output.bmp', output_img)
                    
path = "img.bmp"
size = getsize(path)
print("Size of " + path + " = " + str(size) + " bytes")
path = "index.bmp"
size = getsize(path)
print("Size of " + path + " = " + str(size) + " bytes")
print('PSNR : ' + str(PSNR('output.bmp')))

fp.close()
