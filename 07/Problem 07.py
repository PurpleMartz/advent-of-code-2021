# -*- coding: utf-8 -*-
"""
@author: PurpleMartz
"""
from statistics import median

data = open("Problem 07 Data.txt", "r").read()
"""
data = '''16,1,2,0,4,2,7,1,2,14
'''
"""

data = data[:-1].split(',')
numbers = [int(x) for x in data]

target_value = int(median(numbers)) # rounds down
fuel_needed = 0
for number in numbers:
    fuel_needed += abs(number - target_value)

print("PART 1:", fuel_needed)

def get_cost(n):
    return n * (n + 1) // 2

target_value = int(sum(numbers)/len(numbers))
fuel_needed = 0
for number in numbers:
    fuel_needed += get_cost(abs(number - target_value))

print("PART 2:", fuel_needed)
