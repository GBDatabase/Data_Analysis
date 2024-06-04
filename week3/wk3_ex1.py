numbers = [10,20,30,40,50,60,70,80,90]
### 30~80까지 출력
print(numbers[2:8])

# 10에서 50까지 출력
print(numbers[0:5])

#생략이 가능함
print(numbers[:5])

#60 에서 90까지
print(numbers[5:9])

# 90(끝)도 생략됨.
#60 에서 90까지
print(numbers[5:])

print('----------')

strList = list('Monty Python')
print(strList)
print(strList[0])
print(strList[6:10])
print(strList[-6:-2])
print(strList[:])
print(strList[-50:-50])

print('----------')
#step

print(strList[1::2])
#처음부터끝까지 한개씩
print(strList[::])
