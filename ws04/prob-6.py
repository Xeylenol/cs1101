i = int(input('Enter limit for sequence: '))

a1 = a2 = 1

print(a1)
print(a2)



for x in  range (i-2):
	 a1,a2=a2,(a2+a1)
	 print(a2)
	
print('done')

