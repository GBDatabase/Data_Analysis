#서울의 8월 최고기온 데이터만 추출하여 표현하기


import csv
import matplotlib.pyplot as plt

f =  open('seoul.csv')
data = csv.reader(f)
next(data)

max_temp  = []


for row in data:
    #--------------여기가 문제#
    if row[3]=='' or row[4] =='':
        continue
    if row[4] != "" and row[0].split("-")[1]=='08':
        max_temp.append(float(row[4]))
    if row[4] != "" and row[0].split("-")[1]=='01':
        max_temp.append(float(row[4]))

plt.hist(bins=100, color="b",label="aug" )
plt.hist(bins=100,color="r", label="jan")
plt.legend()