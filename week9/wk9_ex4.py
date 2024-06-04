import csv
f = open('subwayfee.csv')
data = csv.reader(f)
next(data)
maxResult = [0] * 4
maxResult_station = [''] * 4
label = ['유임승차','유임하차','무임승차','무임하차']
for row in data :
    for i in range(4,8) :
        row[i] = int(row[i])
        if row[i] > maxResult[i-4] :
            maxResult[i-4] = row[i]
            maxResult_station[i-4] = row[3] +' '+ row[1]
for i in range(4) :
    print(label[i]+' : '+maxResult_station[i], maxResult[i])