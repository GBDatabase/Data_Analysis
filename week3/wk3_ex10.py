animal = {'강아지' : 'dog','고양이' : 'cat','새' : 'bird','코끼리' : 'elephant'}

while True :
    animal = str(input('동물 이름(한글): '))
    if animal =='끝':
        break
    result = dict.get(animal)
    if result:
        print(animal, '는 영어로는 ',result '입니다.')
    else
        print('동물사전에없서요')

print('프로그램 종료')