#seoul csv파일 읽는법
#csv 라이브러리

import csv
f = open("seoul.csv", encoding='cp949')
data = csv.reader(f, delimiter=',')
#print(data)
cnt = 0
for row in data:
    if row[4] == '':
        cnt += 1
        print(row)


f.close()
print('누락된 데이터: ')