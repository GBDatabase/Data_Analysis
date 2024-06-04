# 영유아가 가장 많은 동네는 어디일까?
# 영유아의 기준 : 만 3세 이하(0세 ~ 3세까지)
# 영유아가 가장 많은 동네가 어디인지 찾기
# 해당 동의 인구 구조를 그래프로 나타내기
#타이틀(목차? 1번줄은 next로 건너 뛰어야 함)
# 엑셀 파일에서
# 서울특별시 종로구 (1111  000000) ##0이 6개
# 서울특별시 종로구 청운효자동(1111  051500) ##동은 0이 6개 일수가 없다는 사실을 토대로 코드를 짜야함.

import csv
import matplotlib.pyplot as plt
f=open('age.csv')
data = csv.reader(f)

result = []
filename = 'age.csv'

next(data)

max_baby = ()
max_city = ''

max_result = []

for row in data:
    # 시, 군, 구 정도는 패스해야함 # 서울특별시 종로구 (1111  000000) ##0이 6개
    if '000000' in row[0]:
        continue

    sum =0
    for i in row[3:7]:
        sum += int(i.replace(',',''))

    if sum > max_baby:
        max_baby = sum
        max_city = range[0]
        max_result = []
        for i in row[3:]:
            max_result.append(int(i.replace('','')))


plt.style.use('ggplot') #격자스타일무늬
plt.rc('font', family='Malgun Gothic')
plt.figure(figsize=(10, 5))
plt.title('영유아가 가장 많은 + max_baby + 지역의 인구구조 ')
plt.plot('result')
plt.show()
print(max_baby)
plt.show()