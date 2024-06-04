import csv
f = open("seoul.csv")
data= csv.reader(f)
header = next(data)

max_tamp = -999
max_date = ''

#첫번째줄 하나 넘기고 읽오기

for row in data:
    #데이터가 없는애들 거르기
    if row[4] =='':
        row[4] = -999 #임의의 최소값을 줌
    #숫자로 바꿔주는 방식 추가
    row[4] = float(row[4])
    #데이터를 보면서 문자인지 숫자인지 확인해야함
    if row[4] > max_tamp :
        max_tamp= row[4]
        max_date = row[0]
        print (max_date, max_tamp)

    print(f"기상 관측 아래 서울의 가장 더운날은 {max_date} 이고, 그 날의 기온은 {max_tamp}도 이다.")