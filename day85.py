#With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

li1 = [1,3,6,78,35,55]
li2 = [12,24,35,24,88,120,155]

new_li = [x for x in set(li1 and li2) if x in li1 and li2]
print(new_li)


#Their Solution

# set1 = set([1,3,6,78,35,55])
# set2 = set([12,24,35,24,88,120,155])
# set1 &= set2

# li = list(set1)
# print(li)