import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
p=float(input("enter pb gain:"))
s=float(input("enter sb gain:"))
pf=float(input("enter pb frq:"))
sf=float(input("enter sb freq:"))

N=0.5*(np.log10(((1/p**2)-1)/((1/s**2)-1))/np.log10(pf/sf))
N=np.ceil(N)
print (N)
wc=pf/(((1/p**2)-1)**(1/2*N))
print (wc)
w=np.arange(0,10000)

mag=[]
for i in range (0,10000):
	s=0
	hw=1/(cm.sqrt(1+((i/sf)**(2*N))))
	mag.append(np.abs(hw))
print (mag)
plt.plot(w,mag)
plt.show()




