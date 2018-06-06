''' Write a program that calculates and prints the value according to the 
given formula:
Q = squareroot of [(2*C*D)/H]
The following are fixed values of C and H, C is 5 and H is 30
D is the variable whose values should be input to your program in a comma-seperated sequence
Example:
Let us assume the following comma-seperated input sequence is given to the program:
100, 150, 180
The output of the program should be: 18,22,24
Hint: if the ouptut received is in decimal form, it should be rounded off
to its nearests value (for example if the output received is 26.0, it should be printed
as 26) in case of input data being supplied to the question it should be assumed to be a console input)'''

import math

c = 50
h = 30
value = []
items = [int(x) for x in input("Enter the value for d: ").split(',')]
for d in items:
    value.append(str(round(math.sqrt((2 * c * float(d)) / h))))
print(','.join(value))
