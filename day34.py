def print_dict():
	values = dict([n,n**2] for n in range(1,21))
	print(values.keys())
	# for k,v in values.items():
	# 	print(k)

print_dict()