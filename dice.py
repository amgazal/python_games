"""A simple die roller

Author: Abdallah Gazal(amg526)
Date: September 2, 2025
"""
import random
first=int(input('Type the first number: '))
last=int(input('Type the last number: '))
x=random.randint(first,last)
y=random.randint(first,last)
print('Choosing two numbers between '+str(first)+' and '+str(last)+'.')
roll=x+y
print('The sum is '+str(roll)+'.')
