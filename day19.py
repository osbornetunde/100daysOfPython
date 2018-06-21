arrange = []
while True:
	values = input("Enter the info: ")
	if not values:
		break
	content = values.split(",")
	name = content[0]
	age = content[1]
	score = content[2]
	# name = sorted(name)
	# if name == sorted(name):
	# 	age = sorted(age)
	# elif age == sorted(age):
	# 	score = sorted(score)
	#sorted_list = sorted(content)
	arrange.append(tuple(content))
print(content)
print(sorted(arrange))