import csv
import matplotlib.pyplot as plt

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = [0] * 24  # 시간대별 최대 승차 인원을 저장할 리스트 초기화
mx_station = [''] * 24  # 시간대별 최대 승차 인원 역 이름을 저장할 리스트 초기화
s_in = [0] * 24      # 승차 인원을 저장할 리스트 초기화
s_out = [0] * 24     # 하차 인원을 저장할 리스트 초기화
for row in data:
    row[4:] = map(int, row[4:])
    for j in range(24):
        s_in[i] += row[4 + j * 2]  # j값과 인덱스 번호 값의 관계식 사용
        s_out[i] +=  row[5 + j * 2]

plt.rc('font', family='Malgun Gothic')
plt.bar(range(24), mx, color='b')  # 막대그래프 속성 변경
plt.xticks(range(24), mx_station, rotation=90)
plt.title('지하철 시간대별 승차인원 추이')
plt.plot(s_in, label="승차")
plt.plot(s_out,label="하자")
plt.legend()
plt.show()