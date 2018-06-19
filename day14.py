# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9











# import string


# upper = []
# lower = []

# values = input("Enter a sentence: ")
# for x in values:
# 	if x in string.ascii_lowercase:
# 		lower.append(x)
# 	elif x in string.ascii_uppercase:
# 		upper.append(x)
# print("Uppercase: %s  \n lowercase: %s" %(len(upper),len(lower)))




#Another solution

s = input()

d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
	if c.isupper():
		d["UPPER CASE"] += 1
	elif c.islower():
		d["LOWER CASE"] += 1
	else:
		pass

print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])