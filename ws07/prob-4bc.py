roll_mark = {} #dict
with open('roll_marks.txt') as f:
    for line in f.readlines():
        # Split line using space as delimeter and remove new line character:
        roll, mark = line.replace('\n', '').split(' ')
        roll_mark[roll] = int(mark)
        
#print(roll_mark)
for i in roll_mark.keys():
	if roll_mark[i] < 50:
		mark = roll_mark[i]+5
		roll_mark[i] = mark
		
		
#print(roll_mark)
with open('new-marks.txt',"w") as f:
	  for i in roll_mark.keys():
	  	f.write(i+" "+str(roll_mark[i])+"\n")   
	  	
with open('failed.txt',"w") as f:
	  for i in roll_mark.keys():
	  	if roll_mark[i] < 50:
	  		f.write(i+"\n")  	 
