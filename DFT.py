import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
j=np.complex(0,1)
x=[4,5,8,1,3,9,10,25,33,20,3]
u=int(input("enter the N to find N pt DFT:"))
c=int(input("no of zeroes to be added:"))
N=len(x)
q=N+c
w=np.arange(0,q)
v=np.arange(0,u)
X=[]
Y=[]
while (N<q):
	x.append(0)
	N+=1
for i in range(0,u):
       s=0
       for k in range(0,N):
            s+=(x[k]*np.exp(-k*2*np.pi*i/N*j))
       X.append(s)
for i in range(0,q):
       s=0
       for k in range(0,len(x)):
            s+=(x[k]*np.exp(-k*2*np.pi*i/N*j))
       Y.append(s)
print (x)
m=np.abs(X)
p=np.angle(X)
a=np.abs(Y)
b=np.angle(Y)
plt.subplot(231)
plt.stem(v,X,'r')
plt.subplot(232)
plt.stem(v,m,'b')
plt.subplot(233)
plt.stem(v,p,'g')
plt.subplot(234)
plt.stem(w,Y,'r')
plt.subplot(235)
plt.stem(w,a,'b')
plt.subplot(236)
plt.stem(w,b,'g')
plt.show()
