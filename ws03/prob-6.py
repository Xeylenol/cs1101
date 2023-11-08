x=[0,3,1,2,8,7,9,0,4,7]

#As we are instructed to use a loop to sort the list, We will use insertion sort, cuz it's the only one i know. ;)
n = len(x) 
	
for i in range(1, n): 
	key = x[i] 
	j = i-1
	while j >= 0 and key < x[j]: 
		x[j+1] = x[j] 
		j -= 1
	x[j+1] = key


#This can also be achived by the use of the inbuilt sort() function, why are we not allowed to use it? :(
#x.sort()
print(x)
