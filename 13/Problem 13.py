# -*- coding: utf-8 -*-
"""
@author: PurpleMartz
"""

data = open("Problem 13 Data.txt", "r").read()
"""
data = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
'''
"""

from enum import IntEnum
class Axis(IntEnum):
    x = 0
    y = 1

def parse_data(data):
    coordinates, fold_instructions = map(lambda chunk: chunk.split('\n'), data[:-1].split('\n\n'))
    coordinates = {tuple(map(int, coordinate.split(','))) for coordinate in coordinates}
    fold_instructions = [instruction[11:] for instruction in fold_instructions]
    return coordinates, fold_instructions

# Using this function, I verified that the fold is always in the middle of the paper.
from operator import itemgetter
def find_max(coordinates):
    return max(coordinates,key=itemgetter(0))[0], max(coordinates,key=itemgetter(1))[1]

def fold_util(coordinate, fold_coordinate, axis):
    value = coordinate[axis]
    if coordinate[axis] > fold_coordinate:
        value = 2 * fold_coordinate - coordinate[axis]
    
    if axis == Axis.x:
        return (value, coordinate[Axis.y])
    else:
        return (coordinate[Axis.x], value)

def fold_on(coordinates, fold_coordinate, axis):
    return {fold_util(coordinate, fold_coordinate, axis) for coordinate in coordinates}

def run_instructions(coordinates, fold_instructions):
    for fold_instruction in fold_instructions:
        axis, fold_coordinate = fold_instruction.split('=')
        fold_coordinate = int(fold_coordinate)
        axis = Axis[axis]
        coordinates = fold_on(coordinates, fold_coordinate, axis)
    return coordinates

coordinates, fold_instructions = parse_data(data)
print("PART 1:", len(run_instructions(coordinates, fold_instructions[:1])))

import matplotlib.pyplot as plt

def visualise(coordinates):
    coordinates = list(coordinates)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.scatter(*zip(*coordinates))
    ax.set_aspect('equal', adjustable='box')
    plt.gca().invert_yaxis()
    plt.show()

new_coordinates = run_instructions(coordinates, fold_instructions)
visualise(new_coordinates)

# Answer: BLKJRBAG