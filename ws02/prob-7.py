#7.1
print("the first sum")
s1 = 0
for n in range(1,6):
	for m in range(1,6):
		a = (((n-m)**2)/((n+m)**2))
		print('n:%1d m:%1d sum:%.2f' %(n,m,a))
		s1=s1+1
print("final Sum is: "+str(a))
print('done')
#7.2
print("the second sum")
s2 = 0
for n in range(1,6):
       for m in range(n+1,6):
              a = (((n-m)**2)/((n+m)**2))
              print('n:%1d m:%1d sum:%.2f' %(n,m,a))
              s2=s2+1
print("final Sum is: "+str(a))
print('done')
print ("The total number of loops in the first and second sum are respectively : %d and %d " %(s1,s2))
