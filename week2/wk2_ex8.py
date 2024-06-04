import random

guess_number = random.randint(1, 100)
print("숫자를 맞혀 보세요. (1~100)")
count = 0
while True:
    try:
        i = int(input())
        count += 1
        if( 1 <= i & i< guess_number):
            print("입력한 숫자가 낮습니다. up시켜서 다시 입력하세요")
        elif (i > guess_number & i <= 100):
            print("입력한 숫자가 높습니다. down시켜서 다시 입력하세요.")
        elif (i == guess_number):
            print("랜덤한 숫자와 같습니다" , count , "번 만에 맞히셨습니다")
            break
    except:
        print('1-100까지의 숫자를 입력하세요')