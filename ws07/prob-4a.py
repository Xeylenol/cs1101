Roll = []
Marks = []

with open('roll_marks.txt') as f:
    for line in f.readlines():
        # Split line using space as delimeter and remove new line character:
        roll, mark = line.replace('\n', '').split(' ')
        Roll.append(roll)
        Marks.append(mark)
        
x = []
for i in Marks:
	x.append(int(i))
#print(x)

#sorting by insertion sort
n = len(x) 
	
for i in range(1, n): 
	key = x[i] 
	j = i-1
	while j >= 0 and key < x[j]: 
		x[j+1] = x[j] 
		j -= 1
	x[j+1] = key
#print(x)
with open('high-marks.txt',"w") as f:
	  f.write(str(x[n-1]))   
