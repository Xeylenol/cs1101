x=[0,3,1,2,8,7,9,0,4,7]


large= x[0]
for i in range(len(x)):
	if large <  x[i]:
		large = x[i]
print('The Largest element: %d' %(large), "and the index is: ", str(x.index(large)))  


#Inbuit function :)
#print(max(x))


small = x[0]

for i in range(len(x)):
        if small >= x[i]:
                small = x[i]
print('The smallest element: %d,'%(small), "and the index is:", str(x.index(small))) 
# the only problem is that we only get the index of the 1st "0" how do we deal with it?? :(

#Inbuit function :)
#print(min(x))
