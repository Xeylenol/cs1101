#6
a1 = a2 = 1
print("  1 %3d" %(a1))
print('  2 %3d' %(a2))
for x in  range (3,31):
	an = a1+a2
	print('%3d %3d' %(x,an))
	a1 = a2
	a2 = an
	
	
print('done')
