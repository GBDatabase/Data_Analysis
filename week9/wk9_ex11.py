import csv
import matplotlib.pyplot as plt

f= open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

subway_station_name = input("역 이름 입력 >> ")

s_in =[0] * 24
s_out =[0] * 24

for row in data:
    if row[3] == subway_station_name:
        row[4:] = map(int, row[4:])
        for i in range(24):
            s_in[i] += row[4+i*2]
            s_out[i] += row[5+i*2]


plt.rc('font', family='NanumGothic')
plt.style.use('ggplot')
plt.figure(figsize=(15, 7))
plt.title(f'{subway_station_name}역 시간대별 승하차 인원 추이')
plt.plot(range(24), s_in, label='승차', color='r')
plt.plot(range(24), s_out, label='하차',  color='b')
plt.legend()
plt.xticks(range(24), [f'{i}' for i in range(4, 28)])
plt.show()

