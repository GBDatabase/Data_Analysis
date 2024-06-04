#matplotlib 라이브러리 임포트해야 사용가능

import matplotlib.pyplot as plt

#그림 데이터
MyGrowth = [130,140,150,165,175,176]
age = [10,12,14,16,18,20]
weight=[25,35,40,55,70,73]

#주어진 데이터로 그래프 그리기    <색상><마커모양><라인스타일> 순으로...
#plt.plot(*args: age, MyGrowth, color="r", linestyle="--")
#plt.plot(age, MyGrowth, color="r", linestyle=":")
#plt.plot(age, MyGrowth, color="r", ls=".")
plt.plot(age, MyGrowth, color="r", ls="r^", label="height")
plt.plot(weight, MyGrowth, color="r", ls="b--", label="weight", linewidth="5")
#print(plt.plot(MyGrowth))


plt.xlabel('age')
plt.xlabel('MyGrowth', fontsize=15)
plt.legend() #범례

plt.show()


