

#import csv
import matplotlib.pyplot as plt
import numpy as np


result = []

for i in range(13):
    result.append(random.randint(1,1000))

print(result)
print(sorted(result))
result2 = np.array(result)
print("1/4: "+str(np.percentile(result2, 25)))
print("2/4: "+str(np.percentile(result2, 50)))
print("3/4: "+str(np.percentile(result2, 75)))
plt.boxplot()
plt.show()