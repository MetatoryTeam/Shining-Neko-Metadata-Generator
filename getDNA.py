import json
import os
import random

f = open("dna.csv", "w")

#Build의 json 디렉토리 내 파일 리스트 변수에 저장
count_JSON = os.listdir("./build/json/")

num = []
dna = []

for i in count_JSON:
    try :
        with open("./build/json/" + i, "r", encoding="utf8", errors='ignore') as json_file:
            json_data = json.load(json_file)
            num.append(i.split(".json")[0])
            dna.append(json_data["dna"])
    except:
        print(i)

def has_duplicates(seq):
    return len(seq) != len(set(seq))
print(has_duplicates(dna))

f.write("NFT Number" + ',' + "DNA" + '\n')
for i in range(len(num)):
    f.write(num[i] + ',' + dna[i] + '\n')

f.close()

#배열내 중복요소가 있는지
#https://ko.from-locals.com/python-list-duplicate-check/