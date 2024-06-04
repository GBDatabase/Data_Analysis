#태어난 해 이후의 최저기온과 최고기온을

import csv
import matplotlib.pyplot as plt

f =  open('seoul.csv')
data = csv.reader(f)
next(data)
high  = []
low = []

for row in data:
    if row[3]=='' or row[4] =='' or int(row[0].split("-")[0]<2000):
        continue
    if row[0].split("-")[1]='05' and  row[0].split("-")[2] = "25":
        high.append(float(row[4]))
        low.appennd(float(row[3]))


    plt.rc(group:"font", family="Malgun Gothic")
    plt.rcparams['axes.unicode_minus'] = False
    plt.title("내 생일 날의 최고기온과 최저기온 추이")
    plt.figure(fontsize=(10,2))
    plt.plot(high,"r")
    plt.plot(low,"b")
    plt.legend()
    plt.show()