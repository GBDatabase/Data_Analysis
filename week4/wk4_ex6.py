#기상관측 이래, 서울의 가장 추웠던 날은 언제였고, 몇 도 였을까?

import csv
f = open("seoul.csv")
data = csv.reader(f)
next(data)

min_temp = 999
min_date = ''

for row in data:
    # 최저 기온이 없는 경우를 고려하여 처리
    if row[3] == '':
        row[3] = 999
    else:
        row[3] = float(row[3])

    # 최저 기온 갱신 여부 확인
    if row[3] < min_temp:
        min_temp = row[3]
        min_date = row[0]

# 결과 출력
print(f"서울의 가장 추웠던 날은 {min_date}이고, 기온은 {min_temp}도였습니다.")

# 파일 닫기
f.close()
