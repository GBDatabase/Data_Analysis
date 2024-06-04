str = "python"

#for 문에는 반드시 시퀀스 자료형이 와야 함
for i in str:
    print(i, end='')
print()
name= ['홍길동','이순신', '유관순']


#i라는 변수
for i in name:
    print(i)

#
# i를 안줄수도 있음
#for _ in range(10): #range(10) = [0,1,2,3,4,5,6,7,8,9]

for i in range(10):  # range(10) = [0,1,2,3,4,5,6,7,8,9]
    print('Hello', i)

for i in range(1,11, 2):
    print(i)