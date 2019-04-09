import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
j=np.complex(0,1)
def dft(x):
	N=len(x)
	X=[]
	for i in range(0,N):
	       s=0
	       for k in range(0,u):
		    s+=(x[k]*np.exp(-k*2*np.pi*i/N*j))
	       X.append(s)
	return X
a=[]
b=[]
x=[]
y1=[]
y2=[]
x1=[3,6,10,44,59,30,54,67,5,2,1]
x2=[1,2,3,4,5,6,7,8,9,10,33]
for i in range(11):
	s=x1[i]+x2[i]
	x.append(s)
	s=0
print x
a=dft(x1)
b=dft(x2)
y1=a+b
y2=dft(x)
m1=np.abs(y1)
m2=np.abs(y2)
plt.subplot(211)
plt.plot(m1,'g')
plt.subplot(212)
plt.plot(m2,'b')
plt.show()	
