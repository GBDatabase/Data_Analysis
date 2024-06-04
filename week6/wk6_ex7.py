import csv
import matplotlib.pyplot as plt

f=open('gender.csv')
data = csv.reader(f)


m=[]
f=[]

for row in data:
    if '신도림' in row[0]:

         # for i in row [3:104]:
         #     m.append(int(i.replace(',','')))
        #
        # for i in row[106:]:
        #     f.append(int(i.replace(',','')))

    for i in range(101):
        m.append(int(row[3+i]))
        f.append(int(row[-i-1])) #리버스는 i앞에 마이너스를 붙이고,  인덱스는 시작은 -1부터 해야해서 하나가 작아야 하므로 -1

print(m)
print(f)
f.reverse()
print(f)

plt.rc('font','Malgun Gothic')
plt.title("신도림 지역의 남여 성별 인구분포 ") #레이블

plt.rcParams['axes.unicode.minus'] = False

plt.barh(range(101, m))# 수평으로 그릴거기 때문에 barh
plt.barh(range(101, f))

plt.legend() #30번 레이블이 보여질려면 legend
plt.show()