#This Python File is deleting "edtion" & "Compiler" part for Trimming JSON File
import json
import os
#Build의 json 디렉토리 내 파일 개수 변수에 저장
count_JSON = len(os.listdir("./build/json/"))
for i in range(1,count_JSON + 1):
    with open("./build/json/" + str(i) + ".json", "r") as json_file:
        json_data = json.load(json_file)
        json_data.pop('edition')
        json_data.pop('compiler')
        with open("./build/json/" + str(i) + ".json", 'w') as outfile:
            json.dump(json_data, outfile, indent=4)

#reference
#https://abluesnake.tistory.com/107
#https://lngnat.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EA%B0%92-%EC%B6%94%EA%B0%80-append-insert-extend-%EC%82%AC%EC%9A%A9
#https://stackoverflow.com/questions/42339876/error-unicodedecodeerror-utf-8-codec-cant-decode-byte-0xff-in-position-0-in
#https://swlock.blogspot.com/2021/10/python-count-files.html
