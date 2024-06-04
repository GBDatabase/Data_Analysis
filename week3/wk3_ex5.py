listData = []

a = 0
while True:
    a = int(input('점수입력 : '))
    if a==0:
        break

        listData.append(a)
    if i < a:
        maxValue = i
    if i > a:
        minValue = i


minValue = listData[0]
maxValue = listData[0]



# for i in listData:
#     if i < a:
#         maxValue = i
#     if i > a:
#         minValue = i


print(list)
print('최대값은', maxValue, '이고,최소값은', minValue, '입니다.')