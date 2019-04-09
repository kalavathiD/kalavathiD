import numpy as np
from matplotlib import pyplot as plt
n=input("enter no.of samples")


p=0
y=[]
for i in range(int(n)):
	p=p+np.sin(i*2*np.pi*5/1000)
	y.append(p)
t=np.arange(0,int(n),1)
plt.plot(t,y)
plt.show()

