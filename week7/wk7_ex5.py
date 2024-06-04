import numpy as np

a= np.array([1,2,3,4])
print(a)
print(type(a))

#숫자와 문자열을 섞음

a= np.array([1,2,'3',4])
print(a)

#
a= np.zeros(10)
print(a)

#연속된 숫자로 데이터를 생성 간으
b= np.arange(3)
print(b)
b=np.arrange(3,7) #step값도 줄 수 있다
b=np.arrange(3,7,2) #step값도 줄 수 있다
print(b)

#연속된 실수값도 배열로 ㅅ생성
c=np.arrange(1,2,0.1)
print(c) #1.9까지

#구간 나누기
d=np.linspace(1,2,11) ##1에서 2사이를 11개의 구간으로 나누기

#mask 기능 = 조건을 만족하는 요소만 선별
a = np.arrange(-5,5)
print(a)
print(a<0) #모든 a값들이 0보다 작은지 비교
print(a[a<0])

#마스크
mask1 = abs(a)>3
print(a[mask1])

#마스크는 복합적으로 두개 이상(2로 나눈 나머지가 0인 즉 짝수인)
mask2=abs(a)%2 ==0
print(a[mask2])
print(a[mask1+mask2]) #or 의 역할을 함. 둘중 하나라도
print(a[mask1*mask2]) #and의 역할을 함

