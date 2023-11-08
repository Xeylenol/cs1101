#a python code that generates values of the function f(x) = sin(2πωx) for 200 values of x uniformly spaced in the domain [−20, 20]
from math import *

w  = 0.1
fx = {}
#dom is [−20, 20] and we need 200 values of x uniformly spaced in it

d = (20 - (-20))/199
d1 = -20
val = []
for i in range(200):
	y = sin(2*pi*w*d1)
	val.append(y)
	fx[d1] = y
	d1 += d
	
X = list(fx.keys())
with open('xfx_sin.dat',"w") as f:
	  for i in X:
	  	f.write(str(i)+"\t"+str(fx[i])+'\n') 
