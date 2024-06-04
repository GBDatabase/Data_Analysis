

#age = this_year - born_year
birth = int(input("태어난 연도를 입력하세요 "))
age = 2024 - birth

if 8 <= age > 26:
    print("학생이 아닙니다")
elif age >= 20:
    print("대학생")
elif age >=17:
    print("고등학생")
elif age >=14:
    print("중학생")
elif age >=8:
    print("초딩학생")
else :
    print("알수없습니다.")


