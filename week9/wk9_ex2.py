import csv

f = open('subwayfee.csv')
data = csv.reader(f)
next(data)  # 첫 줄은 헤더라 넘기기

# 비율이 가장 높은 값을 저장할 변수
mx = 0
# 비율이 가장 높은 역 저장
mx_station = ''

for row in data:
    for i in range(4, 8):  # 4번부터 8번 인덱스까지 전부 정수로 변환
        row[i] = int(row[i])

    # 총 이용자 수 계산
    total = row[4] + row[6]

    # 무임승차가 0이 아니고 총 이용자가 100,000명 이상인 경우에만 계산
    if row[6] != 0 and total >= 100000:
        # 무임승차 비율 계산
        rate = row[6] / total
        # 최대 무임승차 비율 업데이트
        if rate > mx:
            mx = rate
            mx_station = row[1] + ' ' + row[3]
            print(mx_station, round(mx,2))
