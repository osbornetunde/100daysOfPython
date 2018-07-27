#By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155]

lis = [12,24,35,70,88,120,155]

values = [lis[x] for x in range(len(lis)) if x % 2 != 0]
print(values)

#Their solution

# li= [12,24,35,70,88,120,155]
# li = [x for (i,x) in enumerate(li) if i%2!=0]
# print(li)