# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500






# def transact():
# 	netAmount = 0
# 	while True:
# 		request = input("Enter D to deposit or W to withdraw: ") 
# 		if request in ["D" , "d"]:
# 			D = int(input("Enter amount to deposit: "))
# 			netAmount = netAmount + D
# 		elif request in ["W","w"]:
# 			W = int(input("Enter amount to withdraw: "))
# 			netAmount = netAmount - W
# 		else:
# 			break
# 	print("Your account balance: ", netAmount)


# transact()

netAmount = 0
while True:
	s = input()
	if not s:
		break
	values = s.split(" ")
	operation = values[0]
	amount = int(values[1])
	if operation == "D":
		netAmount += amount
	elif operation == "W":
		netAmount -= amount
	else:
		pass
print (netAmount)