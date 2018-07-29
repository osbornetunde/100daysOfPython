#Please write a program which accepts a string from console and print the characters that have even indexes.

# string = (input("Enter a string: "))
# values = "".join([string[x] for x in range(len(string)) if x % 2 == 0])

# print(values)


#Their solution

s = input()
s = s[::2]
print(s)