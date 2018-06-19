# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3




letters = []
Digit = []

for x in input("Enter string and integers: "):
	if x.isdigit():
		Digit.append(x)
	elif type(x) == str:
		letters.append(x)
print("Digits: %s \n letters: %d" %(len(Digit),len(letters))) 


#Another solution

# s = input()

# d = {"DIGITS":0, "LETTERS":0}
# for c in s:
# 	if c.isdigit():
# 		d["DIGITS"] += 1
# 	elif c.isalpha():
# 		d["LETTERS"] += 1
# 	else:
# 		pass
# print("LETTERS", d["LETTERS"])
# print("DIGITS", d["DIGITS"])