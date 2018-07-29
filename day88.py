# Please write a program which count and print the numbers of each character in a string input by console.

# import collections
# string = input("Enter a string: ")

# values = [(x, y) for x, y in collections.Counter(string).items()]

# for item in values:
#     print("{},{}".format(item[0], item[1]))

# Their Solution

dic = {}
s = input()
for s in s:
	dic[s] = dic.get(s,0)+1
print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))