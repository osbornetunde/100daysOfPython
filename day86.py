#With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

lis = [12,24,35,24,88,120,155,88,120,155]
values = [x for x in lis and set(lis) if x in set(lis) and lis]
print(sorted(values)) 

# values = []
# for x in set(lis):
# 	if x in lis:
# 		values.append(x)
# print(sorted(values))

# li = list(set(lis))

#Their Solution

# def removeDuplicate( li ):
#     newli=[]
#     seen = set()
#     for item in li:
#         if item not in seen:
#             seen.add( item )
#             newli.append(item)

#     return newli

# li=[12,24,35,24,88,120,155,88,120,155]
# print (removeDuplicate(li))
