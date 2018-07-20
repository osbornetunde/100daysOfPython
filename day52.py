def divide():
	return 5/0

try:
	divide()
except ZeroDivisionError:
	print ("Division by zero")
except Exception as err:
	print("Exception found")
finally:
	print("Clean up")