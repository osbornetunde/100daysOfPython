"""Write a program which takes 2 digits, x,y as input and generates a 2-dimensional
array. The element value in the i-th row and j-th column of the array should be i * j.
Example:
suppose the following input were given to the program: 3 ,5
output = [[0,0,0,0,0],[0,1,2,3,4],[0,2,4,6,8]]"""




input_for_system = input("Enter the values for x,y to get an array: ")
dimension = [int(x) for x in input_for_system.split(',')]
rowNum = dimension[0]
colNum = dimension[1]

list = [[0 for column in range(colNum)] for rows in range (rowNum)]
for row in range (rowNum):
	for col in range(colNum):
		list[row][col] = row * col
print(list)