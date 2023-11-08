#2.a program that for any value of n, it will generate a list of square of
#integers 1 to n. Choose any value for the integer variable n 
sum = 0
sumsq = 0
n = 10
for i in range (1,n+1):
	print(i,(i**2))
	sum = sum+i
	sumsq=sumsq+(i**2)
print("The sum of number and their squares are respectively: %d, %d" %(sum,sumsq))

#2.b 
x = 3.1415
y = 22
z = 7
a,b,c = ((x/y),(y/z),(z/x))

print ( " (x/y) = %f, (y/z) = %f, (z/x) =%f" %(a,b,c))
print (type(a))
#2.b v
print('%7.3f'%(y/z),'%7.6f'%(y/z))
#2.b vi
for i in range (1,n+1):
	x,y=(i,(i**2))
	print('%4d'%x,'%5d'%y)
