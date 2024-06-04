#질문:기상 관측 이래, 서울의 일교차가 가장 컸던 날과 그날의 기온차는 얼마였을까
#제출 방법
    #소스코드, 결과화면 프린트스크린
#헤더: 날짜[1]	지점[2]	평균기온(℃)[3]	최저기온(℃)[4]	최고기온(℃)[5]

import csv

f= open("seoul.csv", encoding="cp949")
data= csv.reader(f)
header = next(data)

max_temp= -999
min_temp= 999
max_temp_date= '' #일교차가 가장 컸던 말
min_temp_date= '' #일교차가 가장 적었던 날

for row in data:
    #데이터가 없는 애들 거르기
    if row[3] == '' or row[4] == '':
         row[3] = 999
         row[4] = -999

    max_temp_today = float(row[4])
    min_temp_today = float(row[3])


    if max_temp_today > max_temp:
        max_temp = max_temp_today
        max_temp_date = row[0]
        #print (max_temp_date, max_temp)


    if min_temp_today < min_temp:
        min_temp = min_temp_today
        min_temp_date = row[0]
        #print (min_temp_date, min_temp)

# 일교차 계산
v_illghoucha = max_temp - min_temp

# 결과 출력
print(f"서울의 일교차가 가장 컸던 날은 {max_temp_date} 이고,최저기온은 {max_temp},최저기온은 {min_temp}, 그 날의 기온 차이는 {v_illghoucha}도 였습니다")

# 파일 닫기
f.close()

