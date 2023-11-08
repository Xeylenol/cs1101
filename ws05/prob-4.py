# Define a function
# that that takes an input argument x and calculates the quotient q = x//2 and
#remainder r = x%2 and returns q and r
def f(x):
    	#calculating
	q = x//2
	r = x%2
	return q,r


s = int(input('x = '))

a,b = f(s)
print("The quotient is: %d  and the reamainder is: %d " %(a,b))
