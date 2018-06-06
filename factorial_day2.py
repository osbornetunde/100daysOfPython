import time
start_time = time.clock()
def factorial():
	ans=1
	print("Enter an integer: ")
	num = int(input())
	while num > 1:
		ans = ans * num
		num = num - 1
		if num == 1:
			break
	print(ans)

factorial()

# def fact(x):
# 	if x == 0:
# 		return 1
# 	return x * fact(x - 1)



# x =int(input())
# print (fact(x))
stop_time = time.clock() -  start_time 
print(round(stop_time, 5))

