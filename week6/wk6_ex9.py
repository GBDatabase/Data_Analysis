#자기 동네 성별 그래프 그리기

import csv
import matplotlib.pyplot as plt

f = open('gender.csv')
data = csv.reader(f)
next(data)

m=0
f=0
size = [] #size라는 변수에 리스트자료형으로 넣어줄 생각

dong = input("지역 입력 >> ")

for row in data:
    if dong in row[0]:
        for i in range(101):
            m += int(row[i+3].replace(',',''))
            f += int(row[i+106].replace(',',''))
        break
size.append(m)
size.append(f)

plt.rc('font' , family='Malgun Gothic') #없으면 한글 안뜬다
plt.axis('equal')
plt.pie(size,labels=['남','녀'], autopct='%.1f%%')
plt.title(dong + "지역의 남여 성별 비율")
plt.show()


