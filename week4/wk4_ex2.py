#없는 파일 생성을 굳이 할 필요가없이 생성함
outFp = open("c:\Temp\python\data2.txt", 'w')

while True :
    outStr = input("내용 입력 >>")

    if outStr =='':
        break

    outFp.writelines(outStr+"\n")

outFp.close()
print("정상적으로 파일에 씀.")
