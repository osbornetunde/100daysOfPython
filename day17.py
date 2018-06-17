

def transact():
	netAmount = 0
	while True:
		request = input("Enter D to deposit or W to withdraw: ") 
		if request in ["D" , "d"]:
			D = int(input("Enter amount to deposit: "))
			netAmount = netAmount + D
		elif request in ["W","w"]:
			W = int(input("Enter amount to withdraw: "))
			netAmount = netAmount - W
		else:
			break
	print("Your account balance: ", netAmount)


transact()