inFp = open("C:\Temp\python\data1.txt" , 'r', encoding="UTF-8")

while True:
    inStr = inFp.readline()
    if inStr == '':
        break

        print(inStr, end='')

    inFp.close()