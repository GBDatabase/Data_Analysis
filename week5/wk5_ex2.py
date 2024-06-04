import csv
import matplotlib.pyplot as plt

f=open('seoul.csv')
data=csv.reader(f)
next(data)

#서울의 최고기온만 가지고 그리기
result = []


#중간 결측치를 다른값으로 바꾸거나 빼줘야함
for row in data:
    if row[4] =='':
        continue
    result.append(float(row[4]))

plt.plot(result)































