# -*- coding: utf-8 -*-
"""
@author: PurpleMartz
"""

data = open("Problem 02 Data.txt", "r").read()
data = data[:-1].split('\n')

h_position = 0
depth = 0

for coordinate in data:
    direction, size = coordinate.split(' ')
    size = int(size)
    if direction == 'forward':
        h_position += size
    elif direction == 'up':
        depth -= size
    else:
        depth += size
print("PART 1:", h_position * depth)

h_position = 0
depth = 0
aim = 0

for coordinate in data:
    direction, size = coordinate.split(' ')
    size = int(size)
    if direction == 'down':
        aim += size
    elif direction == 'up':
        aim -= size
    else:
        h_position += size
        depth += aim * size
print("PART 2:", h_position * depth)