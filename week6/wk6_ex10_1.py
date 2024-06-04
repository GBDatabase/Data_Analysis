import csv
import matplotlib.pyplot as plt

f = open('gender.csv')
data = csv.reader(f)
next(data)

result = [0, 0, 0, 0, 0, 0, 0]  # 20대 미만, 20대, 30대, 40대, 50대, 60대, 70대 이상에 해당하는 인구 수를 저장할 리스트

dong = input('지역입력 : ')
for row in data:
    if dong in row[0]:
        idx = 0
        for i in range(3, 104):  # 나이 데이터는 3번 인덱스부터 시작합니다.
            cnt = int(row[i].replace(',', ''))  # 연령대에 해당하는 데이터를 정수형으로 변환하여 cnt에 저장
            index = (i -2) // 10  # 세 번째 열은 해당 연령대 전체의 총 인구 수를 나타내는 열
            if index == 0:  # 20대 미만
                result[index] += cnt
            elif 1 <= index < 7:  # 20대부터 70대까지
                result[index] += cnt
            else:  # 70대 이상
                result[6] += cnt

plt.rc('font', family='Malgun Gothic')
plt.title(dong + " 지역의 인구 구조")
plt.pie(result, labels=[' 20대 미만', '20대', ' 30대 ', ' 40대 ', ' 50대 ', ' 60대 ', ' 70대 이상'], autopct="%.1f%%", startangle=90)
plt.legend()
plt.show()
