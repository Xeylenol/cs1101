# a program that takes an integer (a) from the user and then finds the largest positive integer k for which 2 from the user and then finds the largest positive integer k for
#which 2^k < a.

a = int(input('Enter integer a: '))

k = 0
c = 0
while (2**k) < a:
	c = (2**k)
	k+=1
print(c)
