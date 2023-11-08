# Define a function :0
# that that takes an input argument x and calculates the quotient and remainder for (x + 2) ÷ (y+2). ;)
def f(x,y):
    	#calculating e quotient and the remainder for (x + 2) ÷ (y+2)
	q = (x+2)//(y+2)
	r = (x+2)%(y+2)
	return q,r


x = int(input('x = '))
y = int(input('y = '))

#ensuring divide by zero dosen't happen :/
if y == -2:
	print("Invalid value of y")
else:
	a,b = f(x,y)
	print("The quotient is: %d  and the reaminder is: %d " %(a,b))	

