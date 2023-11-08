#generating Fibonnaci sequenced
a1 = a2 = 1
n = int(input('Enter the N: '))
f = open("fibonacci.txt", "w")

f.write("1\n")
f.write("1\n")


for x in  range (3,n):
	an = a1+a2
	f.write('%3d\n' %(an))
	a1 = a2
	a2 = an
	
	
f.close()	
print('done')
