import csv
import matplotlib.pyplot as plt

f = open('gender.csv')
data = csv.reader(f)
next(data)

idx = 0
result = [0, 0, 0, 0, 0, 0, 0]

# for i in range(i, i+10):  # 해당 나이대의 남성과 여성 인구를 누적
#                 m += int(row[i+3].replace(',', ''))  # 3부터 시작하는 이유는 데이터의 3번째 열부터 남성 인구가 시작됨
#                 f += int(row[i+106].replace(',', ''))
# 남자 여자

dong = input('지역입력 : ')
for row in data:
    if dong in row[0]:
        for i in row[3:]:  # 데이터가 3열에서 시작
            cnt = int(i.replace(',', ''))
            index = idx // 10  # 인덱스를 10으로 나눈 몫을 저장해서 10,20,30,40,...90까지 ...
            if idx < 20:
                index = 0
            result[index] += cnt
            idx += 1

        break

plt.rc('font', family='Malgun Gothic')
plt.title(dong + " 지역의 인구 구조")
label = [' 20대 미만 ', ' 30대 ', ' 40대 ', ' 50대 ', ' 60대 ', ' 70대 이상']
plt.pie(result, labels=['20대 미만', '20대', '30대', '40대', '50대', '60대', '70대 이상'], autopct="%.1f%%",
        explode=(0.2, 0.2, 0, 0, 0, 0, 0))
plt.legend()
plt.show()
