# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106




# solution

# a = input()
# n1 = int("%s" % a)
# n2 = int("%s%s" %(a,a))
# n3 = int("%s%s%s" %(a,a,a))
# n4 = int("%s%s%s%s" %(a,a,a,a))
# print(n1+n2+n3+n4)

a = input("Enter an integer value: ")
n1 = int("{}".format(a))
n2 = int("{}{}".format(a,a))
n3 = int("{}{}{}".format(a,a,a))
n4 = int("{}{}{}{}".format(a,a,a,a))

print(n1+n2+n3+n4)
