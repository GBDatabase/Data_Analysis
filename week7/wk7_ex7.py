# 우리 동네의 인구구조와 가장 비슷한 동네는 어디일까?
	#전국에서 우리 동네의 연령별 인구 구조와 가장 비슷한 형태를 가진 지역은어디일까?

# 알고리즘 설계하기
# 데이터읽기
# 궁금한 지역의 이름 입력
# 궁금한 지역의 인구구조 저장
# 궁금한지역의인구구조와 가장 비슷한 인구구조를 가진 지역찾기
# 동시에 시각화 하여 인구 구조 결과 비교

import numpy as np
import matplotlib.pyplot as plt
import csv

f=open('age.csv')
data=csv.reader(f)
next(data)

data=list(data)
home=None

#인구구조가 비슷한이경긔 데이터 변수
minVal = 999999
result_name = ''
result = 0




name = input('지역 입력 >>')
for row in data:
    if name in row[0]:
        home = np.array(row[3:], dtype=int)/int(row[2])



for row in data:
    if int(row[2]) ==0:
        continue

    if '00000' in row[0] or name in row[0]:
        continue

        #서울시 종로구...즉 구로 끝나는 0이 5개 이상 있는 애들은 걸러내야함.
    away = np.array(row[3:],dtype=int)/int(row[2]) #비율로 저장하겠다.
    s = np.sum((home - away) ** 2)

    s=np.sum(home - away)
    if s < minVal :
        minVal = s
        result_name = row[0]
        result = away





#print(home)



plt.style.use('ggplot') #격자스타일무늬
plt.rc('font', family='Malgun Gothic')
plt.title(name + '신도림 지역의 인구구조')
plt.plot(home, label = name)
plt.plot(result, label = result)
plt.legend()
plt.show()


#전국 모든 지역중 한곳(b)
#A와 B의 인구수를 뺌
#뺀 값의 편차(인구수 값 차이를 모두 더함)가 가장 적은 지역이
##중요한 것은 값위가 달라서 생기는 오류
## 예를 들어서 어디는 800에서 1000이고 b지역은 100에서 200 대이면
    ##데이터의 범우가 달라서 직접 비교하기 힘든경우 비율로함.
    ##전체인구의 몇퍼센트가 0세다...0세/연령구간인구수
    ## csv 가보면 숫자가 , 로 되어있으므로
    ## 첫번째 키포인트. 엑셀에서 ,를 숫자로 바꿔야함(이러면 콤마 체크할 필요없음.
    ## 두번째 키포인트.  data=csv.reader(f) 읽으면 for row in data: 읽고나서 데이터를 반복해서 읽기 위해 자료구조를 리스트로 변경해줘야함
    ## 그다음 #인구구조가 비슷한이경긔 데이터 변수
        # minVal = 999999
        # result_name = ''
        # result = 0
    ## 4번. home = np.array(row [3:], dtype=int) / int(row[2])
        #/ int(row[2]) 해줌

    ###문제 발생하므로 제곱을 취해서 합을 구하자
        ###s=np.sum(home - away)가 아닌
        ###s=np.sum((home - away)**2)
    ### 자기 이름 패스
        ###if '00000' in row[0] or name in row[0]: