#By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

array = [[[0 for column in range(8)] for column in range(5)] for column in range(3)]
print(array)