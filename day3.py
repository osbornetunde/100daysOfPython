

# y=dict()
# def squart(x):
# 	while x >= 1:
# 		if x== 0:
# 			return 1
# 		else:
# 			y[x] = x ** 2
# 			x = x-1
# 	return  y #sorted(y.items(), key=lambda x : x[1])
# print((squart(8)))


n = int(input())
d = {} # d=dict()
for i in range(1, n+1):
	d[i]=i*i

print(d)