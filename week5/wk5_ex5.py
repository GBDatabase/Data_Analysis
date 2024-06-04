#태어난 해 이후 생일의 최고 기온을 그래프로 나타내기

import csv
import matplotlib.pyplot as plt

f =  open('seoul.csv')
data = csv.reader(f)
next(data)

result = []

for row in data:
    #태어나기 전 연도는 패스
    if row[4] != "":
        year = row[0].split("-")[0]
        print(year)
        if int(year) < 2000:
            if row[0].split(("-")[0] == '02'):
                if row[0].split("-")[1] == '05':
                    if row[0].split(("-")[2] == "25"):
                #최고기온 값이 존재하고 8월이 ㄴ경우
                result.append(float(row[4]))

plt.figure(figsize=(12,4))
plt.plot(*args:result,"r")
plt.show()