def length():
	s1 = input("Enter first string: ")
	s2 = input("Enter second string: ")
	l1 = len(s1)
	l2 = len(s2)
	if l1 > l2:
		print(s1 + " is longer")
	elif l2 > l1:
		print(s2 + " is longer")
	else:
		print("They are equal")

length()