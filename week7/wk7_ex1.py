import  matplotlib.pyplot as plt

t=[]
p2=[]
p3=[]

for i in range(0,50,2):
    t.append(i/10) #스케일링해서 주는 값
    p2.append((i/10)**2)
    p3.append((i/10)**3)


#그리기
plt.plot(t,t,'r--') #한개씩 그릴때는 가로축에 t, t, 색상값(점선)
plt.plot(t,p2,'bs')
plt.plot(t,p3,'g3')
plt.plot(t,p2,'bs',t,p2,'bs',t,p3,'g3')
plt.show()