from math import pi
def arctan(x,n=5):
	result = 0
	for i in range(n):
		y =((2*i)+1)
		result += ((((-1)**i)*(x**y)/y))
		
	return result	

t = True
i = 1	
while t:
	y = arctan(1,i)
	#print(y)
	if abs(pi-(y*4)) < 0.01:
		t = False
		
		
	else:
		i +=1
		print(i,(y*4),pi)
