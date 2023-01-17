#This Python File is deleting "edtion" & "Compiler" part for Trimming JSON File
import json
import os
import random
#Build의 json 디렉토리 내 파일 리스트 변수에 저장
count_JSON = os.listdir("./build/json/")
#Build의 NFT204 디렉토리 내 이미지 파일 리스트 변수에 저장
count_image = os.listdir("./build/NFT204/")
#Build의 jSonFile 디렉토리 내 파일 리스트 변수에 저장
count_jSonFile = os.listdir("./build/jSonFile/")
result = []
for i in range(len(count_jSonFile)):
    result.append(count_jSonFile[i])
result.sort()
print(result,len(result))