# import math

# class Circle():
# 	# radius = int(input("Enter the radius: "))
# 	def __init__(self, r=""):
# 		self.r = int(input("enter radius: "))
# 	def areas(self):
# 		area = math.pi * (self.r ** 2)
# 		return area

# 		#Alternative Solution

# class Circle():
# 	radius = int(input("Enter the radius: "))
# 	def areas(self):
# 		area = math.pi * (Circle.radius ** 2)
# 		return area

# 		#Alternative Solution

# class Circle():
# 	def areas(self):
# 		radius = int(input("Enter the radius: "))
# 		area = math.pi * (Circle.radius ** 2)
# 		return area

# circle = Circle()
# print(circle.areas())

		#Their Solution

class Circle():
	def __init__(self, r):
		self.radius = r

	def area(self):
		return self.radius**2*3.14

aCircle = Circle(2)
print(aCircle.area())

