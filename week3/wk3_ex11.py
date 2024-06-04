#원의 넓이와 둘레의 길이를 구하는 프로그램
#반지름 입력받아 반지름 10입력받아
#원의 넓이 circle_area()
#원의 둘레 circle_length()
#입력된 반지름이 1보다 작은 경우 프로그램 종료

def circle_area(r):
    return 3.14* r ** 2


def circle_length(radius):
    return 2 * 3.14 * radius


while True :
    r = float(input("원이 반지름을 입력하세요 >> "))

    if r < 1:
        print("반지름은 1보다 커야 합니다. 프로그램을 종료합니다.")
        break

    area = circle_area(r)
    length = circle_length(r)

    print(f"반지름이 {r} :, {area}")
    print(f"둘레의 길이:, {length:.2f}")



