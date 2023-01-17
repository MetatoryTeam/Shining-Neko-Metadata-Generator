import json
import os
import random
import shutil
#Build의 json 디렉토리 내 파일 리스트 변수에 저장
count_JSON = os.listdir("./build/json/")
#Build의 deleted 디렉토리 내 이미지 파일 리스트 변수에 저장
count_deleted = os.listdir("./build/deleted/")
#Build의 jSonFile 디렉토리 내 파일 리스트 변수에 저장
count_jSonFile = os.listdir("./build/jSonFile/")
#Build의 classified 디렉토리 내 이미지 파일 리스트 변수에 저장
count_classified = os.listdir("./build/classified/")

count_deleted.sort()
count_jSonFile.sort()
count_classified.sort()

Body1 = ['Black', 'Blue Sapphire', 'Coral', 'Gold', 'GrapeFruit', 'Green', 'Orange', 'Pink', 'Red', 'SkyBlue', 'Teal', 'White']
Body1_Glossy = ['Black', 'Blue Sapphire', 'Gold', 'Green', 'Red', 'SkyBlue']
Body1_Matte = ['Coral', 'GrapeFruit', 'Orange', 'Pink', 'Teal', 'White']
Body2 = ['Black', 'Blue Sapphire', 'CatBrown', 'Coral', 'Daisy', 'Gold', 'GrapeFruit', 'Green', 'Magenta', 'Navy', 'Orange', 'Pink', 'Purple', 'Red', 'SkyBlue', 'Teal', 'White']

for i in count_deleted:
    try :
        with open("./build/deleted/" + i, "r", encoding="utf8", errors='ignore') as json_file:
            json_data = json.load(json_file)
            attr = json_data["attributes"]
            for j in Body1:
                if attr[0]["value"] == j:
                    shutil.move("./build/deleted/" + i, "./build/classified/" + j + "/" + i)
                    continue
    except:
        print(i)