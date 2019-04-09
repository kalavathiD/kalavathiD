import numpy as np
#from scipy import signal
from matplotlib import pyplot as plt
p=input("enter order of moving avg sys:")
F1=20 #input frq in hz
Fs=2000
t=np.linspace(0,1,1000)
x=np.sin(2*np.pi*5*t)
#x=signal.sin(2*np.pi*(F1/Fs)*t)
#N=np.sin(2*np.pi*(400/Fs)*t)
N=2*np.random.rand(x.shape[0])
u=x+N
y=[]
for i in range(0,u.shape[0]):
	v=np.sum(u[i:i+int(p)])
	y=np.append(y,v/int(p))
	
#print y
plt.subplot(411)
plt.plot(t,x)
plt.subplot(412)
plt.plot(t,N)
plt.subplot(413)
plt.plot(t,u)
plt.subplot(414)
plt.plot(t,y)
plt.show()


