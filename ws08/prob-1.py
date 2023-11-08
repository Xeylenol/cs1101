# a program which takes two integers from the user and returns all prime numbers between the two integers

# This is not an optimized solution and rather the simplest approach to the problem.
 
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if a > b:
	lower = b
	upper = a
else:
	lower = a 
	upper = b
	
# function to check if a number is prime or not
def is_prime(number):
	flag = 0
	if number == 0 or number == 1:
        	flag = 0
	elif number == 2:
        	flag = 1
	else:
		for i in range(2, number):
			if number % i == 0:
				flag = 0
				break
		else:
			flag = 1
	return flag
 
# main loop
primes = []
for i in range (lower,upper+1):
	       	flag = is_prime(i)
	       	while flag:
	       		primes.append(i)
	       		break
	       		
print("the primes between %d and %d are: \n" %(lower,upper),primes)	       		
