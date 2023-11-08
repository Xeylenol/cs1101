i = 1
namelist = []
while i <=5:
	name = input("Enter the Named %d :" %(i))
	namelist.append(name)
	i+=1

f = open("names.txt", "w")

def namevowel(name):
	vow = False
	vowels = ('a', 'e', 'i', 'o', 'u')
	for x in name.lower():
		if x in vowels:
			vow = True
	return vow

for i in namelist:
	if namevowel(i) == True:
		f.write(i+"\n")

f.close()	
print('done')
