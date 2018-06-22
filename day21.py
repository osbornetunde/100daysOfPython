import math


while True:
	s=input("Enter the positions: ")
	if not s:
		break

	values = s.split(" ")
	positions = values[0]
	steps = int(values[1])
	if positions == "UP":
		y2 = steps
	if positions == "DOWN":
		y1 = steps
	if positions == "LEFT":
		x2 = steps
	if positions == "RIGHT":
		x1 = steps
distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
print(round(distance))