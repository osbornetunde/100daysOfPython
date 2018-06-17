letters = []
Digit = []

for x in input("Enter string and integers: "):
	if x.isdigit():
		Digit.append(x)
	elif type(x) == str:
		letters.append(x)
print("Digits: %s \n letters: %d" %(len(Digit),len(letters))) 