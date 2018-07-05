numbers = [1,2,3,4,5,6,7,8,9,10]

# def squared(x):
# 	n = x**2
# 	return n

# squaredNumber = list(map(squared, numbers))

# print(squaredNumber)

squaredNumber = list(map(lambda x: x**2, numbers))
print(squaredNumber)