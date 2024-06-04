#Pandas 라이브러리 이용
#반드시 인스톨 후 사용
import pandas as pd
import numpy as np


index = pd.date_range('1/1/2000', periods=8)
print(index)

df = pd.DataFrame(np.random.rand(8,3))
print(df)

df = pd.DataFrame(np.random.rand(8,3), index = index, columns=list('ABC'))
#데이터에 접근하기
print(df['8'])

#칼럼을 이용해서 연산하기
df['D'] = df['A']/df['B']
print(df)

df['E'] = np.sum(df,axis=1) #행의 방향으로 더하는지 ...행별로 더하기는 1, 컬럼은 0

mask1 = df['B'] > 0.4
df2 = df[mask1]
print('mask 적용한 df2')
print(df2)

#전체값을 나눠서 파일로 저장하는 기능
#df의 모든값을 c칼럼의 값으로 나눔
df = df.div(df['C'],axis= 0 ) #열단위로...
df.to_csv('test.csv')
print(df)