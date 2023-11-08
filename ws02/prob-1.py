#1.a
x ="The quick brown fox jumps over the lazy dog"
#1.b Check whether the word fox is in this sentence
if  "fox" in x:
	print("Fox is in"+' '+x)
else:
	print("couldn't find the word")
#1.c Print the characters in reverse order
print(x[::-1])
#1.d Print every third character of the above sentence
print(x[2:len(x):3])


