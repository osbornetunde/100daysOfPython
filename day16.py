odd = []

values = [int(x) for x in input("Enter a comma seperated value: ").split(',')]
for x in values:
	if x%2 != 0:
		y = x**2
		odd.append(str(y))
		print(odd)
	else:
		print("not odd")
print(','.join(odd))