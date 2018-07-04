# def print_list():
# 	values = dict([n,n**2] for n in range(1,21))
# 	items = []
# 	# for k,v in values.items():
# 	# 	items.append(v)
# 	for v in values.values():
# 		items.append(v)
# 	print(items)

# print_list()


# def print_list():
# 	li = list(n**2 for n in range(1,21))
# 	print(li)

# print_list()

#Their solution

def printList():
	li = list()
	for i in range(1,21):
		li.append(i**2)
	print(li)


printList()