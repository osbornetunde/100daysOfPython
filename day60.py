"""Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1"""

def f(n):
	if n==0:
		return 0

	else:
		return f(n-1)+100

n = int(input())
print(f(n))