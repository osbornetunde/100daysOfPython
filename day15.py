# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106







# a = int(input("Enter an integer value: "))
# aa = a * 2
# aaa = a * 3
# aaaa = a * 4 
# sum = a + int(aa) + int(aaa) + int(aaaa)
# print("sum: ", sum)


# solution

a = input()
n1 = int("%s" % a)
n2 = int("%s%s" %(a,a))
n3 = int("%s%s%s" %(a,a,a))
n4 = int("%s%s%s%s" %(a,a,a,a))

print(n1+n2+n3+n4)