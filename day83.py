#By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
lis = [12,24,35,70,88,120,155]
# values = [lis[x] for x in range(len(lis)) if x!=0 and x!=4 and x!=5]
# print(values)


# values = [y for (x,y) in enumerate(lis) if x!=0 and x!=4 and x!=5]
# print(values)

#Their solution
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print (li)