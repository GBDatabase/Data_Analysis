import csv
import matplotlib.pyplot as plt


f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)


mx = [0] * 24               # 시간대별 최대 승차 인원 저장 리스트 초기화
mx_station = [''] * 24      # 시간대별 최대 승차 인원 역 이름 저장 리스트 초기화

for row in data:
    row[4:] = map(int, row[4:])

    for i in range(24):
        a = row[4+i*2]  # i와 인덱스 번호 사이의 관계식 사용

        if a > mx[i]:
            mx[i] = a
            mx_station[i] = row[3]

print(mx_station)

plt.rc('font', family='Malgun Gothic')
plt.style.use('ggplot')
plt.figure(figsize=(8,9),dpi=80)
plt.bar(range(24), mx) #0시부터 24니까
plt.xticks(range(24), mx_station, rotation=90) #90도로 꺾어서 표현하면 겹치지 않음
plt.show()


