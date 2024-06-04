#numpy 라이브러리
#숫자 데이터를 쉽게 다루는데 용이
import numpy as np
import matplotlib.pyplot as plt

t=np.arrange(0.,5.,0.2) #간격을 소수점까지 줄수 있다. 0부터 5까지 0.2 간격으로
print(t)
plt.plot(t,'bs',t,t**2,'bs',t,t**3,'g3')
plt.show