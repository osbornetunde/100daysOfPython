# numbers =[1,2,3,4,5,6,7,8,9,10]
# squaredNumbers = map(lambda x: x**2, numbers)
# evenSquaredNumbers = list(filter(lambda x: x%2==0, squaredNumbers))
# print(evenSquaredNumbers)


#Their solution

li = [1,2,3,4,5,6,7,8,9,10]

evenNumbers = list(map(lambda x: x**2, filter(lambda x: x%2==0, li)))
print(evenNumbers)