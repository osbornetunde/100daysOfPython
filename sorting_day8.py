'''Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world'''




word = input("Enter a list of words: ")
list = sorted(word.split(','))
print(','.join(list))

####Another Solution

# items = [x for x in input("Enter a list of words: ").split(',')]
# items.sort()
# print(','.join(items))
