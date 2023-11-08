#define x^0.95
def x95pow(x):
	y = x**(0.95)
	return y
	
#start with x = 10
x = 10
i= 0 #iteration counter
while x>2: #How many iterations do we need to perform until we get x < 2?
	x = x95pow(x)
	i +=1
	
print("The number of iteration required are: ",i)
