
sentence = input("Enter a sentence: ").split(" ")
values= dict(sorted([x,sentence.count(x)] for x in set(sentence)))
for k, v in values.items():
	print(k +":"+ str(v))
