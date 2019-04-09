import numpy as np
import matplotlib.pyplot as plt
n=int(input('enter length '))
x=[]
y=[]
for i in range(n):
	k=input('enter elements:')
	x.append(k)
plt.subplot(3,1,1)
plt.stem(x)
z=n
for i in range(z):
	g=x[z-1-i]
	y.append(g)
print (y)
t=np.arange(0,n,1)
plt.subplot(3,1,2)
plt.stem(t,y)#inverse of a string
p=[]
q=n+z-1
while n<q:
	y.append(0)
	n=n+1
s=0
for i in range(q):
	for j in range (z):
		s=s+(int(x[j])*int(y[i-j]))
	p.append(s)
	s=0
print (p)
plt.subplot(3,1,3)
plt.stem(p)
plt.show()
