#Write a program that takes an integer n as input and produce a file, named factorial.txt
#containing the first n real numbers together with their factorial. 

n = int(input('Enter the N: '))
f = open("factorial.txt", "w")
def factorial(num):	
	factorial = 1
	if num == 0:
		factorial = 1
	else:
		for i in range(1,num + 1):    
			factorial = factorial*i    
	
	return factorial

for i in range (n+1):
	fac = factorial(i)
	f.write('%3d %3d\n' %(i,fac))
	
f.close()
