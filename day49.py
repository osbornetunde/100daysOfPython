class American():
	@staticmethod
	def printNationality():
		print("I am a Nigerian")

class NewYorker(American):
	print("i am a new NewYorker")

newyork = NewYorker()
newyork.printNationality()