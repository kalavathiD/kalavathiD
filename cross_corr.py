import numpy as np
import matplotlib.pyplot as plt
n=int(input('enter the length n:'))
m=int(input('enter the length m:'))
x=[]
y=[]
h=[]
p=[]
q=n+m-1
for i in range(n):
	k=input('enter elements:')
	x.append(k)
for i in range(m):
	k=input('enter elements:')
	y.append(k)
z=m
for i in range(z):
	g=y[z-1-i]
	h.append(g)
while m<q:
	h.append(0)
	m=m+1
s=0
for i in range(q):
	for j in range (n):
		s=s+(int(x[j])*int(h[i-j]))
	p.append(s)
	s=0
print (p)
t=np.arange(0,q,1)
plt.stem(p)
plt.show()




