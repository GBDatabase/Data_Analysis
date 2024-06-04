import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

mx = 0               # 최댓값을 저장할 변수 초기화
mx_station = ''      # 최댓값을 갖는 역 이름 저장 변수 초기화

#출근 시간대(7~9시)에 가장 많이 내리는 곳?
for row in data :    # 최댓값 찾기(전부 탐색하여 최댓값을 갱신하는 방식)
    row[4:] = map(int, row[4:])
    total = row[11:16:2]
    if sum(total) > mx :
        mx = sum(total)
        mx_station = row[3]+'('+row[1]+')'
print(mx_station, mx)