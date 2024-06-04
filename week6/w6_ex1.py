import csv
import matplotlib.pyplot as plt

f=open('age.csv')
data = csv.reader(f)

result = []

for row in data:
    if '신도림' in row[0]:
        #print(row)
        # 엑셀 1번줄 4번째는 D이고 찾고자 하는 "2023년12월_계_0세" 이니 인덱스 번호는 [3].
        for i in result[3:]:
            result.append(int(i))

print(result)
plt.style.use('ggplot') #격자스타일무늬
plt.rc('font', family='Malgun Gothic')
plt.figure(figsize=(10, 5))
plt.title('신도림 지역의 인구구조')
plt.plot.use('result')
plt.show()
