import json
import os
import random
#Build의 json 디렉토리 내 파일 리스트 변수에 저장
count_JSON = os.listdir("./build/json/")
#Build의 deleted 디렉토리 내 이미지 파일 리스트 변수에 저장
count_deleted = os.listdir("./build/deleted/")
#Build의 jSonFile 디렉토리 내 파일 리스트 변수에 저장
count_jSonFile = os.listdir("./build/jSonFile/")

count_deleted.sort()
count_jSonFile.sort()

Body1 = ['Black', 'Blue Sapphire', 'Coral', 'Gold', 'GrapeFruit', 'Green', 'Orange',  'Red', 'SkyBlue', 'Teal', 'White']
Body1_Glossy = ['Black', 'Blue Sapphire', 'Gold', 'Green', 'Red', 'SkyBlue']
Body1_Matte = ['Coral', 'GrapeFruit', 'Orange', 'Pink', 'Teal', 'White']
Body2 = ['Black', 'Blue Sapphire', 'CatBrown', 'Coral', 'Daisy', 'Gold', 'GrapeFruit', 'Green', 'Magenta', 'Navy', 'Orange', 'Pink', 'Purple', 'Red', 'SkyBlue', 'Teal', 'White']

list_204 = ['100.json', '102.json', '114.json', '115.json', '127.json', '130.json', '143.json', '148.json', '15.json', '150.json', '151.json', '153.json', '155.json', '161.json', '165.json', '173.json', '18.json', '182.json', '186.json', '189.json', '197.json', '212.json', '214.json', '219.json', '232.json', '238.json', '246.json', '25.json', '254.json', '26.json', '261.json', '267.json', '269.json', '272.json', '276.json', '280.json', '282.json', '284.json', '285.json', '288.json', '289.json', '300.json', '302.json', '307.json', '310.json', '311.json', '314.json', '317.json', '319.json', '32.json', '328.json', '329.json', '332.json', '333.json', '334.json', '336.json', '339.json', '344.json', '346.json', '35.json', '357.json', '36.json', '361.json', '371.json', '374.json', '376.json', '39.json', '392.json', '393.json', '399.json', '40.json', '400.json', '406.json', '409.json', '411.json', '414.json', '418.json', '419.json', '421.json', '422.json', '423.json', '432.json', '436.json', '442.json', '446.json', '458.json', '471.json', '473.json', '474.json', '477.json', '490.json', '491.json', '502.json', '503.json', '513.json', '515.json', '519.json', '529.json', '533.json', '534.json', '535.json', '546.json', '549.json', '550.json', '551.json', '560.json', '564.json', '565.json', '568.json', '572.json', '579.json', '588.json', '602.json', '606.json', '607.json', '612.json', '613.json', '615.json', '617.json', '622.json', '649.json', '651.json', '66.json', '665.json', '666.json', '670.json', '671.json', '672.json', '673.json', '675.json', '677.json', '679.json', '68.json', '684.json', '685.json', '70.json', '704.json', '707.json', '708.json', '716.json', '717.json', '718.json', '725.json', '726.json', '728.json', '735.json', '736.json', '737.json', '738.json', '739.json', '740.json', '742.json', '748.json', '75.json', '760.json', '767.json', '776.json', '789.json', '790.json', '797.json', '799.json', '805.json', '816.json', '82.json', '822.json', '824.json', '825.json', '826.json', '832.json', '833.json', '841.json', '844.json', '847.json', '848.json', '85.json', '855.json', '869.json', '874.json', '881.json', '882.json', '885.json', '887.json', '894.json', '90.json', '902.json', '905.json', '907.json', '91.json', '914.json', '921.json', '927.json', '938.json', '948.json', '954.json', '957.json', '958.json', '966.json', '973.json', '975.json', '976.json', '981.json', '983.json', '993.json', '999.json']
for i in count_deleted:
    try:
        if i in list_204:
            os.remove("./build/deleted/" + i)
    except:
        print(i)