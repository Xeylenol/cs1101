
Name = []
Marks = []
name_mark = {} #dictionary for key value pair of marks and names

#open the file 
with open('wsP\prob5\Grades2.dat') as f:
    for line in f.readlines():
        # Split line using tab as delimeter
        name,mark = line.split('\t')
        Name.append(name)
        Marks.append(int(mark))
        name_mark[name] = int(mark)
	
	
#print(name_mark)

def sort_students(name_mark):
	# Convert dictionary to list of tuples
	students = list(name_mark.items())
	
	# Sort list of tuples by mark and then by name
	students_sorted = sorted(students, key=lambda student: (-student[1], student[0]))
	
	return students_sorted

# Call the function
sorted_students = sort_students(name_mark)	



#Generating an output file where the grades are written in a descending order in the first column and the corresponding names in the second column
with open('wsP\prob5\sorted_marks.txt',"w") as f:
	#writing the key value pairs in the file
	  for key,value in sorted_students:
		  f.write(str(value) + '\t' + key + '\n')

