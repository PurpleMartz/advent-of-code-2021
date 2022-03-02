# -*- coding: utf-8 -*-
"""
@author: PurpleMartz
"""

data = open("Problem 05 Data.txt", "r").read()
"""
data = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''
"""

instructions = data[:-1].split('\n')

def parse_instruction(instruction):
    start, end = instruction.split(' -> ')
    x1, y1 = start.split(',')
    x1, y1 = int(x1), int(y1)
    x2, y2 = end.split(',')
    x2, y2 = int(x2), int(y2)
    return x1, x2, y1, y2

storage = dict()    
for instruction in instructions:
    x1, x2, y1, y2 = parse_instruction(instruction)
    if x1 == x2 or y1 == y2:
        x_start = min(x1, x2)
        x_end = max(x1, x2)
        y_start = min(y1, y2)
        y_end = max(y1, y2)
        for x in list(range(x_start, x_end + 1)):
            for y in list(range(y_start, y_end + 1)):
                if (x, y) in storage:
                    storage[(x, y)] += 1
                else:
                    storage[(x, y)] = 1

n_danger = len(list(filter(lambda x: x > 1, storage.values())))
print("PART 1:", n_danger)
   
def update_dict(point_storage, x, y):
    if (x, y) in point_storage:
        point_storage[(x, y)] += 1
    else:
        point_storage[(x, y)] = 1
    return point_storage

def iterate_points_line(points_storage, x_start, x_end, y_start, y_end):
    x_incr = 1 if x_start < x_end else -1
    y_incr = 1 if y_start < y_end else -1
    for x in list(range(x_start, x_end + x_incr, x_incr)):
        for y in list(range(y_start, y_end + y_incr, y_incr)):
            points_storage = update_dict(points_storage, x, y)
    return points_storage

def iterate_points_diagonal(points_storage, x_start, x_end, y_start, y_end):
    x_incr = 1 if x_start < x_end else -1
    y_incr = 1 if y_start < y_end else -1
    y = y_start
    for x in list(range(x_start, x_end + x_incr, x_incr)):
        points_storage = update_dict(points_storage, x, y)
        y += y_incr
    return points_storage
        
storage = dict()    
for instruction in instructions:
    x1, x2, y1, y2 = parse_instruction(instruction)
    if x1 == x2 or y1 == y2:
        storage = iterate_points_line(storage, x1, x2, y1, y2)
    elif abs(x1 - x2) == abs(y1 - y2):
        storage = iterate_points_diagonal(storage, x1, x2, y1, y2)
        
n_danger = len(list(filter(lambda x: x > 1, storage.values())))
print("PART 2:", n_danger)