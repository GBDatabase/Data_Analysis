#ex2번 폴더 그대로 가져온후 30번 barchat 고치기

#지역명을 입력받아 연령별 인구수 데이터 시각화 하기
# 인구 구조가 알고싶은 지역의 이름(읍면동 단위) 의 단위를 입력해 주세요 : 구갈동 <<입력
import csv
import matplotlib.pyplot as plt

f=open('age.csv')
data = csv.reader(f)

result = []

i = input("인구 구조가 알고싶은 지역의 이름(읍면동 단위) 의 단위를 입력해 주세요 : ")
f=open('age.csv')
data = csv.reader(f)

result = []

for row in data:
    if '신도림' in row[0]:
        #print(row)
        # 엑셀 1번줄 4번째는 D이고 찾고자 하는 "2023년12월_계_0세" 이니 인덱스 번호는 [3].
        for i in result[0:]:
            result.append(int(i.replace(',','')))


print(result)
plt.style.use('ggplot') #격자스타일무늬
plt.rc('font', family='Malgun Gothic')
plt.figure(figsize=(10, 5))
plt.title('신도림 지역의 인구구조')
plt.bar(range(101), result)
plt.show()