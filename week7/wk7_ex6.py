#버블 차트 그리기
import matplotlib.pyplot as plt
import random
import numpy as np

x=[]
y=[]
size=[]

x=np.random.randint(-100,100, 1000)
y=np.random.randint(-100, 100, 1000)

mask1 = abs(x)>50 #절대값이 50보다 큰 애들만 가져오기
mask2 = abs(y)>50

x=x[mask1+mask2]
y=y[mask1+mask2]

size=np.random.randint(len(x)) *100

plt.scatter(x,y,s=size,c=size,cmap='iet',alpha=0.6) #color값도 줌, 단 x값이 변하는 것에 따라서 값이 변함(기준값이 x,y,size 줄 수 있음,cmap는 색상(iet, ocean, 중복되는 값이 안보이면 alpha값을 준다)
plt.show()