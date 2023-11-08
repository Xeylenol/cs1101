# Define a function which takes the three lengths (as arguments) and determines whether these sticks can form a triangle :|
def tri(a,b,c):
	if (((a+b)>c and (b+c)>a) and ((c+a)>b)): #three lengths form a triangle if the sum of any two lengths is greater than the third.
		return True
	else:
		return False


#user input ;0
print("Enter the lengths of the sides of the triangle.")
a = int(input("input Length A: "))
b = int(input("input Length B: "))
c = int(input("input Length C: "))

#Giving output to the user :)
triangle = tri(a,b,c)
if triangle:
	print("The triangle is possible")
else:
	print("The triangle is not possible")
