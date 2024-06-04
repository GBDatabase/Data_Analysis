def calc(v1,v2, op) :
    result = 0
    if op == '+' :
        result = v1 +v2
    elif op == '-' :
        result = v1- v2
    if op == '*' :
        result = v1 * v2
    elif op == '/' :
        result = v1 / v2
    return result

##전역변수
res = 0
var1, var2, oper = 0,0, '' #초기화

#메인코드
oper = int(input("계산할 연산자는? (+-/*)")
var1 = int(input("첫 번째 수 입력 >> ")
var2 = int(input("두 번째 수 입력 >> ")
res = calc(var1, var2, oper)
print(f"result =  {res}")