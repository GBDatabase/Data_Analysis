inFp, outFp = None, None
inStr = ''

inFp = open("c:/Windows/win.ini", "r")
outFp = open("c:\Temp\python\data3.txt", 'w')

inlist = inFp.readlines()

for inStr in inlist:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("파일이 정상적으로 복사함")