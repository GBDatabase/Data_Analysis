#버블 차트 그리기
import matplotlib.pyplot as plt
import random

x=[]
y=[]
size=[]

for i in range(200):
    x.append(random.randint(10,100))
    y.append(random.randint(10, 100))
    size.append(random.randint(10, 100))

plt.scatter(x,y,s=size,c=size,cmap='iet',alpha=0.6) #color값도 줌, 단 x값이 변하는 것에 따라서 값이 변함(기준값이 x,y,size 줄 수 있음,cmap는 색상(iet, ocean, 중복되는 값이 안보이면 alpha값을 준다)
plt.show()