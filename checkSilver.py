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

count_image.sort()
count_jSonFile.sort()

Body1 = ['Black', 'Blue Sapphire', 'Coral', 'Gold', 'GrapeFruit', 'Green', 'Orange',  'Red', 'SkyBlue', 'Teal', 'White']
Body1_Glossy = ['Black', 'Blue Sapphire', 'Gold', 'Green', 'Red', 'SkyBlue']
Body1_Matte = ['Coral', 'GrapeFruit', 'Orange', 'Pink', 'Teal', 'White']
Body2 = ['Black', 'Blue Sapphire', 'CatBrown', 'Coral', 'Daisy', 'Gold', 'GrapeFruit', 'Green', 'Magenta', 'Navy', 'Orange', 'Pink', 'Purple', 'Red', 'SkyBlue', 'Teal', 'White']

result = []
silver = []
final_result = []
dna = []
for i in count_JSON:
    try :
        with open("./build/json/" + i, "r", encoding="utf8", errors='ignore') as json_file:
            json_data = json.load(json_file)
            attr = json_data["attributes"]
            if attr[-1]["value"] == "Silver" and attr[0]["value"] != "Gold":
                silver.append(i)
    except:
        print(i)
result.sort()
silver.sort()
samplelist = random.sample(silver, 79)
samplelist.sort()
print("Result : ", silver, len(silver))
#print("samplelist : ", samplelist, len(samplelist))

    
#os.remove()
#reference
#https://abluesnake.tistory.com/107
#https://lngnat.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EA%B0%92-%EC%B6%94%EA%B0%80-append-insert-extend-%EC%82%AC%EC%9A%A9
#https://stackoverflow.com/questions/42339876/error-unicodedecodeerror-utf-8-codec-cant-decode-byte-0xff-in-position-0-in
#https://swlock.blogspot.com/2021/10/python-count-files.html
#os.rename('Entiy01.txt','career.Entity01.txt') ('기존','바꾸고 싶은 이름 ')