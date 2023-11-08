a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

def check(a,b,c):
    if (a+b) <= c or (b+c)<=a or (c+a)<=b:
        return False
    return True
   

if check(a,b,c) is True:
	print("The triangle is possible")
else:
	print("The triangle is not possible")
