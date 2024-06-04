#자기 동네 성별 그래프 그리기

# 20대 미만 70대 이상 , 20대랑 30대는 강조 표시
#
# 70대 이상f
# 30
# 40
# 50
# 60
# 70대 이상


import csv
import matplotlib.pyplot as plt

f = open('gender.csv')
data = csv.reader(f)
next(data)


idx = 0
result = [0,0,0,0,0,0,0]



dong = input('지역입력 : ')
for row in data:
    if dong in row[0]:
        for i in row[3:]: #데이터가 3열에서 시작
            cnt=int(i.replace(',',''))
            index = idx // 10 #인덱스를 10으로 나눈 몫을 저장해서 10,20,30,40,...90까지 ...
            if index >= 6: ##작업 1 . 이게 없으면 outofrange 오류가 뜸
                index = 6 ##작업 1
            result[index] += cnt #여기서 -1을 해야함?
            idx += 1

        break


plt.rc('font' , family='Malgun Gothic')
plt.title(dong + " 지역의 인구 구조")
label = [' 20대 미만 ', ' 30대 ', ' 40대 ', ' 50대 ', ' 60대 ', ' 70대 이상']
plt.pie(result, labels=['20대 미만','20대','30대','40대','50대','60대','70대 이상'], autopct="%.1f%%", explode=(0.2, 0.2, 0, 0, 0, 0, 0))
plt.legend()
plt.show()


