import os
import pandas as pd
import json

## 한 디렉토리의 이미지의 이름을 읽어 DataFrame으로 반환하는 함수

def loadImage(path):

    file_list = os.listdir(path)

    img_list = pd.DataFrame(file_list,columns=['file_name'])

    return img_list

## 해당 디렉토리에서 중복을 검사하고 이미지를 저장
### 현재 미구현

def saveImage(img, path):
    path
