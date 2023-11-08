#def funcn

def repfk (n):
	a1 = a2 = 1
	y = 2
	for i in range (0,n-1):
		an = a1+a2
		y += (an**-1)
		a1 = a2
		a2 = an
	return y


		
n = 1
with open('convergence.dat',"w") as f:
	while abs(repfk(n)-3.359885666243) >= 0.000001:
		#f.write(str(n)+"\t"+str(abs(repfk(n)-3.359885666243))+'\n') #abs_diff
		f.write(str(n)+"\t"+str(repfk(n))+'\n')
		n+=1
		
	
print(n)
