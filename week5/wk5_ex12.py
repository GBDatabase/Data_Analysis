#서울의 최고기온 데이터를 월별로 정리해서 기록한다.
    #데이터를 월별로 분류해서 저장
    #데이터를 boxplot으로 나타내기

import csv
import matplotlib.pyplot as plt



f =  open('seoul.csv')
data = csv.reader(f)
next(data)

month= [[], [], [], [], [], [], [], [], [], [], [], []]
cnt= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ]

for row in data:
    if row[4]=='':
        continue
        index = int(row[0].split('-')[1])
        month[index-1].append(float(row[4]))
        cnt[index-1] += 1
plt.boxplot(month)
print(cnt)
plt.show()



