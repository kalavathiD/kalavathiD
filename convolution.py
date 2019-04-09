import numpy as np
import matplotlib.pyplot as plt
x=int(input("enter length of x:"))
y=int(input("enter length ofy:"))
m=[]
n=[]
p=[]
q=x+y-1
t=np.arange(0,q,1)
for i in range (x):
	c=input ("enter an elements:")
	m.append(c)
for i in range (y):
	d=input("enter an elements:")
	n.append(d)
while y<q:
	n.append(0)
	y=y+1
print(n)
s=0
for i in range (q):
	for j in range (x):
		s=s+(int(m[j])*int(n[i-j]))
	p.append(s)
	s=0
print(p)
plt.stem(t,p)
plt.show()

	
