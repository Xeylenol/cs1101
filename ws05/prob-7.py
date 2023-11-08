from math import *

#Define a function which takes an argument t (in degrees) and returns sin 2t
def sin2t(t):
	d= sin((t*pi)/90) #sin 2t 
	return d

#no need to take input	
#t = int(input("enter value of t in degrres: "))

print("t, sin(2t)")
#loop which uses the function to print θ,sin 2θ for θ = 0, 10, 20, 30, . . . , 80, 90 :)
for i in range(0,100,10):
	print("%d , %1.5f " %(i,sin2t(i)))
	

