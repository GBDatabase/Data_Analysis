import csv

f = open('subwayfee.csv')
data = csv.reader(f)
next(data) #ValueError: invalid literal for int() with base 10: '유임승차' 해결

#비율이 가장 높은 값 저장
mx = 0
#비율이 가장 높은 역 저장
rate = 0
mx_station = ''

for row in data :
    for i in range(4,8) : #4번부터 8번 인덱스까지 전부 바꿈
        row[i] = int(row[i])

    total = row[4] + row[6]
    if row[6] != 0 and (row[4] + row[6]) > 100000:
        rate = row[4] / total
    # if row[6] == 0 and total >= 100000:
    #     continue  
        if rate > mx:  # 만약 rate 값이 mx 값보다 크다면
            mx = rate  # 만약 mx 값을 rate 값으로 업데이트하기
            mx_station = row[1] + ' ' + row[3]
            print(mx_station, round(mx,2))

