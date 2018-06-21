class Generator():
	def __init__(self):
		self.iterated = []

	def get_input(self):
		self.n = int(input("Enter an integer: "))
		return self.n

	def iterate(self, n):
		for i in range(0,n):
			if i%7 == 0:
				self.iterated.append(i)
		print(self.iterated)

generator = Generator()
value = generator.get_input()
generator.iterate(value)