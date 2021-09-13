import matplotlib.pyplot as plt
import random
import math

def power_distribution(n = 100, alpha = 1.6):
    x=[]
    for i in range(n):
        u = random.uniform(0,1)
        rand = - 14.85 + 15.85*u
        x.append(pow(1.-rand,-1./(alpha-1.)))
    return x

x = power_distribution(1000000)
print(x)

'''
y = plt.hist(x, bins=1000, range= (0.01, 100)) #[0.01, 0.1, 1, 10,100]
plt.xscale('log')
plt.show()
'''