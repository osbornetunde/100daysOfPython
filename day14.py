import string


upper = []
lower = []

values = input("Enter a sentence: ")
for x in values:
	if x in string.ascii_lowercase:
		lower.append(x)
	elif x in string.ascii_uppercase:
		upper.append(x)
print("Uppercase: %s  \n lowercase: %s" %(len(upper),len(lower)))