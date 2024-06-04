#BMI는 몸무게(kg) /키(m^2)
#몸무게, 키를 화면으로 입력받아 계산함.
#소수점 이하 2자리까지 표현한다


weight = int(input("당신의 몸무게(kg)를 입력하세요 >>"))
height = int(input("당신의 키(cm)를 입력하세요 >> "))
height_m =height / 100
bmi = weight / (height_m**2)

print("당신의 BMI 지수는 = " , bmi , "입니다.")
print("bmi = %.2f" % bmi)
print("bmi = {:2}".format(bmi))
print("bmi  = ", round(bmi,2))