color1 = ['red','blue','green']
color2 = ['orange','black','white']
print(color1 + color2)
total = color1+color2
print(total)


print(len(total))

#곱셈
print(color1*2)

print('blue' in color1)
print('blue' in color2)



#리스트에 추가 및 삭제
#print(color1-color2)

#append()
#append()는 항상 맨 뒷쪽에 추가됨.
color1.append('white')
print(color1)

#extend() : 리스트를 추가
color1.extend(color2)
print(color1)
color2.extend('black')
print(color2)
color2.extend(['black'])
print(color2)

#insert() : 위치를 지정해서 값을 추가

color = ['red', 'blue', 'green']
color.insert(__index=0, __object='purple')
print(color)

#remove() : 특정 값을 삭제
color.remove('purple')
print(color)

color[0] = 'purple'
print(color)

del color[0]
print(color)

