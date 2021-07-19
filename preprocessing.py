import cv2 as cv
import progressbar
import numpy as np

import file_module

'''
def nothing(x):
    pass
'''

img_dir = "E:/data/Item-Image"
save_dir = "E:/data/masked-Image"

img_list = file_module.loadImage(img_dir)

bar = progressbar.ProgressBar(maxval=len(img_list)).start()
for index, row in img_list.iterrows():

    img_path = img_dir +'/'+ row['file_name']
    save_path = save_dir +'/'+ row['file_name']

    '''
    cv.namedWindow('binary')
    cv.createTrackbar('threshold', 'binary', 0, 255, nothing) 
    cv.setTrackbarPos('threshold', 'binary', 230)
    '''

    img_color = cv.imread(img_path)
    img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)

    while(True): 
        
        #low = cv.getTrackbarPos('threshold', 'binary') 

        ret,img_binary = cv.threshold(img_gray, 230, 255, cv.THRESH_BINARY_INV)

        #cv2.threshold( grayscale image, threshold_value, value, flag{cv2.THRESH_BINARY_INV : pixle 값이 threshold_value 보다 크면 0, 작으면 value로} )
  
        #cv.imshow('binary', img_binary)
        #cv.imshow("color", img_color)
        cv.imwrite(save_path, img_binary)

        #if cv.waitKey(1)&0xFF == 27: # esc 누르면 닫음
        break
    bar.update(index-1)

print("process complete")