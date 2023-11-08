import math 

pi = math.pi
# exp funcn
def sum_exp(n,x):
    term = 1.0
    store = term 
    for i in range(1,n):
        term = (x/i)*term
        store = store + term
    return store
    
    
#a program which findsthe number of terms required to compute the value of π (using the above series) correct upto an absolute difference of 10^-4
t = True
i = 1
v = math.exp(pi)
#print(v)
while t:
	y = sum_exp(i,pi) 
	#print(y,v)
	if abs(v-(y)) < 0.0001:
		t = False
		#print(abs(v-(y)) ,i)
		
	else:
		i +=1
		#print(v,y,i)

#print the number of iteration required (value of n), the exact value of π, the computed value of π and their absolute difference.

print("The number of iteration required= ", (i-1))
print('The Exact Value of = ', v)
print("The Computed Value S= " , (y))
print("their absolute difference is = ", abs(v-(y)))

