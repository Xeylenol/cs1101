x=[0,3,1,2,8,7,9,0,4,7]

large= x[0]

for i in range(len(x)):
	if large <  x[i]:
		large = x[i]
print('The Largest element: %d' %(large), "and the index is: ", str(x.index(large)))

#using inbuilt function :)
#print(max(x))
