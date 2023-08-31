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

print(DeleteAllfiles('/content/sample.xlsx'))
print(DeleteAllfiles('/content/beforeWinner.xlsx'))

pd.set_option('display.max_rows', 10000)

print('이전 파일을 업로드해주세요')
uploaded = files.upload()
beforeWinnerDf = pd.read_excel('beforeWinner.xlsx')
thisMonth = int(input('몇월 인가요?'))
num = int(input('몇명을 뽑으시나요?'))
print('현재 파일을 업로드해주세요')
uploaded = files.upload()
df = pd.read_excel('sample.xlsx')

beforeWinnerCheckDec = {1:[10,11,12,1],2:[11,12,1,2],3:[12,1,2,3],4:[1,2,3,4],5:[2,3,4,5],
                        6:[3,4,5,6],7:[4,5,6,7],8:[5,6,7,8],9:[6,7,8,9],10:[7,8,9,10],11:[8,9,10,11],12:[9,10,11,12]}
thisMonthCheck = beforeWinnerCheckDec[thisMonth]
isBeforeWinner = beforeWinnerDf[(beforeWinnerDf['month'] == thisMonthCheck[0]) | (beforeWinnerDf['month'] == thisMonthCheck[1]) | (beforeWinnerDf['month'] == thisMonthCheck[2]) | (beforeWinnerDf['month'] == thisMonthCheck[3]) ]
beforeWinnerList = isBeforeWinner['email'].values.tolist()

total_count = df['name'].count()-1
for i in range(num):
  winner = df['email'][randint(0,total_count)]
  while winner in beforeWinnerList:
    winner = df['email'][randint(0,total_count)]
  beforeWinnerList.append(winner)
print('🌷신청자 명단🌷')
print(df)

print('추첨중.....')
print('.....')
print('ヽ（≧□≦）ノ')
print('🌼 당첨을 축하드립니다.🌼 ')
for i in beforeWinnerList[-num:]:
  isWinner = df['email'] == i
  winner = df[isWinner]
  beforeWinnerDf =  beforeWinnerDf.append({'email':winner['email'].values[0],'name':winner['name'].values[0],'team':winner['team'].values[0],'month':thisMonth},ignore_index = True)

  print(winner['team'].values[0],'팀의 ',winner['name'].values[0],'님 !!! email : ',winner['email'].values[0])

print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
beforeWinnerDf.to_excel('beforeWinner.xlsx',index=False)
