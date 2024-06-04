#승차인원이 가장 많은 역은 어디일까?
#승차인원 = 유임승차 + 무임승차

import csv

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)  # 첫 줄은 헤더라 넘기기

# 가장 많은 총 승차 인원 저장할 변수
max_total = 0
# 가장 많은 총 승차 인원을 가진 역
max_station = ''

for row in data:
    for i in range(4, 8):  # 4번부터 8번 인덱스까지 전부 정수로 변환
        row[i] = int(row[i])

    # 유임승차와 무임승차를 합한 총 승차 인원 계산
    total = row[4] + row[6]

    # 최대 총 승차 인원 업데이트
    if total > max_total:
        max_total = total
        max_station = row[1] + ' ' + row[3]

        print(max_station, max_total)
