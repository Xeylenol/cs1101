#function f(x, n) which calculates the above series upto nth term for a given x.
import math
#value of natural logarithm of 1 + x
def lnf(x,n=5):
	result = 0
	if abs(x) < 1:
		for i in range(n):
			y =(i+1)
			result += ((((-1)**i)*(x**y)/y))
	else:
		return False
	return result	
	

#a program which findsthe number of terms required to compute the value of π (using the above series) correct upto an absolute difference of 10^-2
t = True
i = 1
v = math.log(0.75)
print(v)
while t:
	y = lnf((-0.25),i) #1+x = 0.75
	#print(y)
	if abs(v-(y)) < 0.01:
		t = False
		#print(abs(v-(y)) ,i)
		
	else:
		i +=1
		#print(y,i)

#print the number of terms required (value of n), the exact value of π, the computed value of π and their absolute difference.

print("The number of terms required= ", (i-1))
print('The Exact Value of ln(0.75)= ', v)
print("The Computed Value of ln(0.75)= " , (y))
print("their absolute difference is = ", abs(v-(y)))
