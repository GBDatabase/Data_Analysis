import matplotlib.pyplot as plt
import csv
f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
result = []


for row in data :
    row[4:] = map(int, row[4:]) #일괄적으로 데이터에 특정함수를 적용할 때 사용 , map(적용할 함수명, 함수에 적용할 데이터)
    #print(row)
    result.append(row[10])
    print(result)
    print(len(result))

result.sort()
plt.bar(range(len(result)), result)
plt.show()