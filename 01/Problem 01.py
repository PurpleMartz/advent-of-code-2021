# -*- coding: utf-8 -*-
"""
@author: PurpleMartz
"""

data = open("Problem 01 Data.txt", "r").read()
data = data[:-1].split('\n')
numbers = [int(x) for x in data]

counter = 0
for i in range(len(numbers) - 1):
    if numbers[i + 1] - numbers[i] > 0:
        counter += 1
print("PART 1:", counter)

counter = 0
for i in range(len(numbers) - 3):
    if numbers[i + 3] - numbers[i] > 0:
        counter += 1
print("PART 2:", counter)
