import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df= pd.read_csv('age.csv',encoding='cp949', index_col=0)
#print(df.head())

#나눠줄때는 분모가 0이되면 안되므로 0이 아닌 애들만 처리...#필요없으니까 컬럼지움
#마스크처럼 처리하겠음
mask1= df['2023년12월_계_연령구간인구수']>0
df = df[mask1]

# df = df.div(df['2023년12월_계_연령구간인구수'],df['2023년12월_계_총인구수']
# ,axis=0)

name = input('지역 입력 >>')
a = df.index.str.contains(name)
df2=df[a]
print(df2)

#각각의 비율을 지역별로 뺀 값이 저장
x = df.sum(df2.iloc[0],axis=1)

#차이를 제곱
y= np.power(x,2)
z=y.sum(axis=1)

#인구구조가 가장 유사한 상위 5곳을 그래프로 그리기
i = z.sort_values().index[:5]
df.loc[i].T.plot() #i를 가지고 찾아야 하니까
plt.rc('font' , family='Malgun Gothic')
plt.show()
#df2.T.plot()
plt.show()