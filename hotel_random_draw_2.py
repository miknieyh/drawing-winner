# 예비후보 / 핸드폰번호
import pandas as pd
from google.colab import files
from random import *
import os

def DeleteAllfiles(filePath):
    if os.path.exists(filePath):
        os.remove(filePath)
        return '초기화 완료'
    else:
        return ''

print(DeleteAllfiles('/content/sample2.xlsx'))
print(DeleteAllfiles('/content/beforeWinner2.xlsx'))

pd.set_option('display.max_rows', 10000)

print('이전 파일을 업로드해주세요')
uploaded = files.upload()
beforeWinnerDf = pd.read_excel('beforeWinner2.xlsx')
thisMonth = int(input('몇월 인가요?'))
num = int(input('몇명을 뽑으시나요?'))
print('현재 파일을 업로드해주세요')
uploaded = files.upload()
df = pd.read_excel('sample2.xlsx')

beforeWinnerCheckDec = {1:[10,11,12,1],2:[11,12,1,2],3:[12,1,2,3],4:[1,2,3,4],5:[2,3,4,5],
                        6:[3,4,5,6],7:[4,5,6,7],8:[5,6,7,8],9:[6,7,8,9],10:[7,8,9,10],11:[8,9,10,11],12:[9,10,11,12]}
thisMonthCheck = beforeWinnerCheckDec[thisMonth]
isBeforeWinner = beforeWinnerDf[(beforeWinnerDf['month'] == thisMonthCheck[0]) | (beforeWinnerDf['month'] == thisMonthCheck[1]) | (beforeWinnerDf['month'] == thisMonthCheck[2]) | (beforeWinnerDf['month'] == thisMonthCheck[3]) ]
beforeWinnerList = isBeforeWinner['phonenumber'].values.tolist()

total_count = df['name'].count()-1
for i in range(num):
    winner = df['phonenumber'][randint(0,total_count)]
    while winner in beforeWinnerList:
        winner = df['phonenumber'][randint(0,total_count)]
    beforeWinnerList.append(winner)

print('🌷신청자 명단🌷')
print(df)

print('추첨중.....')
print('.....')
print('ヽ（≧□≦）ノ')
print('🌼 당첨을 축하드립니다.🌼 ')
for idx,i in enumerate(beforeWinnerList[-num:]):
    isWinner = df['phonenumber'] == i
    winner = df[isWinner]
    new_row = pd.DataFrame({'no': [idx+1],
                            'name': [winner['name'].values[0]],
                            'phonenumber': [winner['phonenumber'].values[0]],
                            'month': [thisMonth],
                            '당첨': ['당첨']})
    beforeWinnerDf = pd.concat([beforeWinnerDf, new_row], ignore_index=True)
    print(winner['name'].values[0],'님 !!!  phonenumber : ',winner['phonenumber'].values[0])

print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
for i in range(num):
    winner = df['phonenumber'][randint(0,total_count)]
    while winner in beforeWinnerList:
        winner = df['phonenumber'][randint(0,total_count)]
    beforeWinnerList.append(winner)

print('예비후보 추첨중.....')
print('.....')
print('ヽ（≧□≦）ノ')
print('🌼 예비후보를 축하드립니다.🌼 ')

for idx,i in enumerate(beforeWinnerList[-num:]):
    isWinner = df['phonenumber'] == i
    winner = df[isWinner]
    new_row = pd.DataFrame({'no': [idx+1],
                            'name': [winner['name'].values[0]],
                            'phonenumber': [winner['phonenumber'].values[0]],
                            'month': [thisMonth],
                            '당첨': ['예비후보']})
    beforeWinnerDf = pd.concat([beforeWinnerDf, new_row], ignore_index=True)

    print(winner['name'].values[0],'님 !!!  phonenumber : ',winner['phonenumber'].values[0])

print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
beforeWinnerDf.to_excel('beforeWinner2.xlsx',index=False)
