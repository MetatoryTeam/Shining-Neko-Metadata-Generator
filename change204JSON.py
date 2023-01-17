#This Python File is deleting "edtion" & "Compiler" part for Trimming JSON File
import json
import os
#Build의 jSonFile 디렉토리 내 파일 개수 변수에 저장
count_JSON = os.listdir("./build/jSonFile/")

Body1 = ['Black', 'Blue Sapphire', 'Coral', 'Gold', 'GrapeFruit', 'Green', 'Orange', 'Pink', 'Red', 'SkyBlue', 'Teal', 'White']
Body2 = ['Black', 'Blue Sapphire', 'CatBrown', 'Coral', 'Daisy', 'Gold', 'GrapeFruit', 'Green', 'Magenta', 'Navy', 'Orange', 'Pink', 'Purple', 'Red', 'SkyBlue', 'Teal', 'White']

for i in count_JSON:
    try :
        with open("./build/jSonFile/" + i, "r", encoding="utf8", errors='ignore') as json_file:
            json_data = json.load(json_file)
            json_data.pop('edition')
            json_data.pop('compiler')
            with open("./build/jSonFile/" + i, 'w', encoding="utf8", errors='ignore') as outfile:
                json.dump(json_data, outfile, indent=4)
    except:
        print(i)

for i in count_JSON:
    try :
        with open("./build/jSonFile/" + i, "r", encoding="utf8", errors='ignore') as json_file:
            json_data = json.load(json_file)
            json_data["attributes"][2]["trait_type"] = "Skin 1"
            skin2 = {}
            skin2["trait_type"] = "Skin 2"
            skin2["value"] = "Glossy"
            json_data["attributes"].insert(3, skin2)
            with open("./build/jSonFile/" + i, 'w', encoding="utf8", errors='ignore') as outfile:
                json.dump(json_data, outfile, indent=4)
    except:
        print(i)

#reference
#https://abluesnake.tistory.com/107
#https://lngnat.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EA%B0%92-%EC%B6%94%EA%B0%80-append-insert-extend-%EC%82%AC%EC%9A%A9
#https://stackoverflow.com/questions/42339876/error-unicodedecodeerror-utf-8-codec-cant-decode-byte-0xff-in-position-0-in
#https://swlock.blogspot.com/2021/10/python-count-files.html