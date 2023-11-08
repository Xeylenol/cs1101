#e a python code that generates values of the function f(x) = exp(−x^2/σ) for 100 values of x uniformly spaced in the domain [−5, 5]. Choosing σ = 4 and stores the function values in a list.
from math import *

b = 4
fx = {}
#dom is [−5, 5] and we need 100 values of x uniformly spaced in it

d = (5-(-5))/99
d1 = -5
val = []
for i in range(100):
	y = exp((-d1**2)/b)
	val.append(y)
	fx[d1] = y
	d1 += d

#print(fx)	
#print(val)
#find the maximum fmax from the list containing the values of the function f(x)
nval = val
nval.sort()
fmax = nval[-1]
#print(fmax)

#find the value(s) of x* for which f(x*) ≈ 1/2 fmax.

dif = []
for i in nval:
	dif.append(abs(i-(fmax/2)))
	
dif_min = min(dif)
index_min = dif.index(dif_min)

X = list(fx.keys())

x1 = X[index_min-1]
f1 = val[index_min]
print(x1, f1) #1.6666666666666723 0.49935178859927865 and -1.6666666666666723 0.49935178859927865

with open('xfx.dat',"w") as f:
	  for i in X:
	  	f.write(str(i)+"\t"+str(fx[i])+'\n') 
