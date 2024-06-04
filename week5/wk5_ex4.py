#매년 돌아오는 내 생일의 최고기온을 그래프로 나타내기
import csv
import matplotlib.pyplot as plt

f =  open('seoul.csv')
data = csv.reader(f)
next(data)

result = []
for row in data:
    if row[4] != "":
        if row[0].split("-")[1] == '05':
            if row[0].split(("-")[2] == "25"):
            #최고기온 값이 존재하고 8월이 ㄴ경우
            result.append(float(row[4]))

plt.figure(figsize="10",2)
plt.plot(*args:"result", color="r")
plt.show()


