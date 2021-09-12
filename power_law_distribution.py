import matplotlib.pyplot as plt
import random
import math

def power_distribution(n = 100, alpha = 1.6):
    x=[]
    for i in range(n):
        rand = random.uniform(0,1)
        u = - 14.85 + 15.85*rand
        x.append(pow(1.-u,-1./(alpha-1.)))
    return x

x = power_distribution()
print(x)

y = plt.hist(x, bins=[0.01, 0.1, 1, 10,100])
plt.show()