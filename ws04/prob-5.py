q = 1
a =  int(input("Enter the number: "))
#since a prime number is divisible by one and itself we start checking from 2 
i = 2
if a == 1:
	print(a,' is a number')
elif a <= 0:
	print(a," not defined")
elif a > 1:
	while i <= a**(0.5):
		if a%i == 0:
			q+=1
			break
		i+=1
if q == 1:
	print(a, " is not a prime." )
elif q == 1:
	print(a, " is a prime")
