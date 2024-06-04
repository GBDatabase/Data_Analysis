import csv
import matplotlib.pyplot as plt

plt.rc('font' , family='Malgun Gothic')
size=[2441,2312,1031,1233]
label = [ 'A형' , 'b형' , 'o형' , 'ab형' ]
color = [ 'darkmagenta' , 'deeppink' , 'hotpink' , 'pink' ]

plt.axis('equal')
plt.pie(size, labels=label, colors=color,autopct='%.1f%%', explode=(0,0,0.1,0))  #강조하기 위해서 startangle=90 은 생략

plt.legend()
plt.show()


