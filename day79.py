#Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

lis = [5,6,77,45,22,12,24]

values = [x for x in lis if x%2!=0]
print(values)