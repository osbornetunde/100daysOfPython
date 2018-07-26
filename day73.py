#Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive
import random

print(random.sample([x for x in range(1,1001) if x%5==0 and x%7==0],5))