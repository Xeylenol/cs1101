x=[-1,-3,7,9,-4,3,8,9,-2]

large= x[0]
for i in range(len(x)):
	if large <  x[i]:
		large = x[i]
print('The Largest element: %d' %(large), "and the index is: ", str(x.index(large)))
#print(max(x))

small = x[0]
for i in range(len(x)):
        if small >= x[i]:
                small = x[i]
print('The smallest element: %d,'%(small), "and the index is:", str(x.index(small)))
#print(min(x)) 

#Copy and pasted from problem 6.(i used insertion sort) :0
n = len(x) 
	
for i in range(1, n): 
	key = x[i] 
	j = i-1
	while j >= 0 and key < x[j]: 
		x[j+1] = x[j] 
		j -= 1
	x[j+1] = key


#x.sort() #:( inbuilt function.
print("The sorted list is ", str(x))
