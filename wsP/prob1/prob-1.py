
Name = []
Marks = []
name_mark = {} #dictionary for key value pair of marks and names

#open the file 
with open('Grades1.dat') as f:
    for line in f.readlines():
        # Split line using tab as delimeter
        name,mark = line.split('\t')
        Name.append(name)
        Marks.append(int(mark))
        name_mark[int(mark)] = name
        
x = Marks
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

#Generating an output file where the grades are written in a descending order in the first column
# and the corresponding names in the second column
with open('sorted_marks.txt', "w") as f:
	for i in range(n):
		mk = x[n-1-i]
		nm = name_mark[mk]
		f.write(str(mk) + "\t" + nm + '\n')

