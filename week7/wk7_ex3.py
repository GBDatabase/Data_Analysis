import numpy as np
#반복문을 쓰지않고 한줄로 처리할수있다
#수업시간상 다 알수는 없지만 어떻게 활용할수있는지 연구하면 좋을것 같다고 하심

#rand() 0~1사이에 있는 n개의 실수가 랜덤하게 생성
a = np.random.rand(5)
print(a)
print(type(a))  #출력결과 :<class 'numpy.ndarray'>
##넘파이에서 만들어지면 출력결과에 콤마가 없다. plt와 다르다는 것을 알수있다.

#choice 함수
b= np.random.choice(6,10) #0에서 5까지의 값만 나오는데 랜덤한 10개
print(b)

#주사위 던지기
c= np.random.choice(range(1,7), 10)
print(c)

#중복을 허용하지 않는 경우
d = np.random.choice(10, 6, replace=False)
print(d)

#확률적용
e = np.random.choice(6,10,p=[0.1,0.2,0.3,0.2,0.1,0.1]) #확률을 줌, 0이 나올 확률은 0.1, 1이 나올 확률은 0.2
print(e)

