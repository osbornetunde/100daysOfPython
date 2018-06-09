"""Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world"""
				
lines = []
while True:
	s = input()
	if s:
		lines.append(s.upper())
	else:
		break;


for sentence in lines:
	print(sentence)

				#Another solution

# characters =[]
# while True:
# 	character = input("Enter words: ")
# 	if character:
# 		characters.append(character)
# 	else:
# 		break
# text = '\n'.join(characters)
# print(text)
# case = text.upper()
# #print(case)

#print(''.join(case))
