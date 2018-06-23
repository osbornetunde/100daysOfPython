
sentence = input("Enter a sentence: ").split(" ")
values= dict(sorted([x,sentence.count(x)] for x in set(sentence)))
# for k, v in values.items():
# 	print(k +":"+ str(v))


# def word_count(str):
#     counts = dict()
#     words = sorted(str.split())

#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1

#     return counts
# you = str(input("Enter a string: "))
# print(word_count(you))
