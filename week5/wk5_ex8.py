import random
import matplotlib.pyplot as plt

dice= []
for i in range(100):
    num = random.randint(1,6)
    dice.append(num)

plt.hist(dice,bins=6)
plt.show()