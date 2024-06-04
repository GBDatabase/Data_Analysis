#전국에서 20대가 가장 많은 동네는 어디일까 (20세는 엑셀에서 X는 인덱스 번호는 23번

import csv
import matplotlib.pyplot as plt

f=open('age.csv')
data = csv.reader(f)

result = []

for row in data:
    for i in result[23:]:
        #print(row)
        # 엑셀 1번줄 4번째는 D이고 찾고자 하는 "2023년12월_계_0세" 이니 인덱스 번호는 [3].
            result.append(int(i.replace(',','')))


print(result)
plt.style.use('ggplot') #격자스타일무늬
plt.rc('font', family='Malgun Gothic')
plt.figure(figsize=(10, 5))
plt.title('신도림 지역의 인구구조')
plt.plot('result')
plt.show()