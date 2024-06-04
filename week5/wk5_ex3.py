import csv
import matplotlib.pyplot as plt

f =  open('seoul.csv')
data = csv.reader(f)
next(data)

result = []
for row in data:
    if row[4] != "":
        if row[0].split("-")[1] == '08':
            result.append(float(row[4]))

plt.figure(figsize=10,2)
plt.plot(*args:result,color= "r")
plt.show()
#
#
# str="hello python"
#
# print(str.split())
#
# date = "2024-04-02"
# print(date.split())
