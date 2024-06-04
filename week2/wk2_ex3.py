#동전교환하기
# 7777원을 500원 100원 50원 자리 동전으로 교환

#교환할 금액 입력

money = int(input("교환할 금액 입력 >> "))
print("교환할 금액 : ", money )
## main 부분
money = int(input("교환할 돈은 얼마?"))
coin_500 = money // 500
money %= 500 # 500으로 나눈 나머지
coin_100 = money // 100
money %= 100 # 100으로 나눈 나머지
coin_50 = money // 50


print('500원 짜리 :  %d 개' %coin_500)
print('100원 짜리 :  %d 개' %coin_100)
print('50원 짜리 :  %d 개' %coin_50)
print('잔돈\t==> %d 원' %money)