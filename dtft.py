import numpy as np
import matplotlib.pyplot as plt

j=np.complex(0,1)
#for discrete inputs
#x=[0,1,1,1,1]

#for sin input 
b=np.arange(0,10*np.pi,0.5)
z=5*(np.sin(b))
#print(z)

a1=plt.subplot(3,1,1)
plt.stem(b,z)
#plt.stem(x)

x=z
xmag=[]
xphase=[]
N=1000

w=np.linspace(-np.pi,np.pi,N)
s=0
for i in range(0,N):
	for k in range (0,len(x)):
			s=s+(x[k]*np.exp(-k*w[i]*j))
	xmag.append(np.abs(s))
	xphase.append(np.angle(s))
	s=0
plt.subplot(3,1,2)
plt.plot(w,xmag)
plt.subplot(3,1,3)
plt.plot(w,xphase)

plt.show()












