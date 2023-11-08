#function f(x, n) which calculates the above series upto nth term for a given x.
from math import pi

def arctan(x,n=5):
	result = 0
	for i in range(n):
		y =((2*i)+1)
		result += ((((-1)**i)*(x**y)/y))
		
	return result	
	
			
#x= int(input("Enter x: "))
#n= int(input("Enter n: "))
#print(arctan(x,n)*180)/pi)



#a program which findsthe number of terms required to compute the value of π (using the above series) correct upto an absolute difference of 10^-2
t = True
i = 1
while t:
	y = arctan(1,i)
	#print(y)
	if abs(pi-(y*4)) < 0.01:
		t = False
		#print((y*4)-pi,i)
		
	else:
		i +=1
		#print(y*4,i)

#print the number of terms required (value of n), the exact value of π, the computed value of π and their absolute difference.

print("The number of terms required= ", (i-1))
print('The Exact Value of pi= ', pi)
print("The Computed Value of pi= " , (y*4))
print("their absolute difference is = ", abs(pi-(y*4)))
