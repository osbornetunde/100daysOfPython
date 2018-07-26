#Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.




def binarySearch(list, item):
	bottom = 0
	top = len(list) - 1
	while  bottom <= top:
		mid = int((top + bottom)/2.0)
		if list[mid]==item:
			return mid
		elif list[mid] > item:
			top = mid - 1
		else:
			bottom = mid + 1
	return None

list = [2,5,7,9,11,17,222]
print(binarySearch(list, 11))
print(binarySearch(list, 12))