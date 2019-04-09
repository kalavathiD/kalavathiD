import numpy as n
a=[]
r=input ("Enter no of rows:")
c=input ("ENter no of columns:")
for i in range(0,r,1):
	b=[]
	for j in range (0,c,1):
		b.append(input("Enter a number:"))
	a.append(b)
print a
try:
    inv=n.linalg.inv (a)
except numpy.linalg.LinAlgError:
    pass
else:
    inv=n.linalg.inv (a)
print "Inverse of a given matrix is:\n",inv

