# -*- coding: utf-8 -*-
"""
@author: PurpleMartz
"""

data = open("Problem 09 Data.txt", "r").read()
"""
data = '''2199943210
3987894921
9856789892
8767896789
9899965678
'''
"""

data = data[:-1].split('\n')
numbers = [list(map(int, list(n))) for n in data]
dirs = {'row': [-1, 0, 1, 0], 'col': [0, 1, 0, -1]}

from itertools import product

def get_neighbours(matrix, row, col, max_row, max_col):
    neighbours = set()
    for i in list(range(4)):
        i_row = row + dirs['row'][i]
        i_col = col + dirs['col'][i]
        if 0 <= i_row <= max_row and 0 <= i_col <= max_col:
            neighbours.add(matrix[i_row][i_col])
    return neighbours

def get_low_points(matrix):
    ROW, COL = len(matrix), len(matrix[0])
    low_points = []

    for row, col in product(range(ROW), range(COL)):
        current = matrix[row][col]
        neighbours = get_neighbours(matrix, row, col, ROW - 1, COL - 1) 

        if all(neighbour > current for neighbour in neighbours): 
           low_points.append(current)
    return low_points 

def get_risk_levels_sum(matrix):
    low_points = get_low_points(matrix)
    return sum(low_points) + len(low_points)

print("PART 1:", get_risk_levels_sum(numbers))


def get_low_point_coord(matrix, ROW, COL):
    low_point_coords = []

    for row, col in product(range(ROW), range(COL)):
        neighbours = get_neighbours(matrix, row, col, ROW - 1, COL - 1) 

        if all(neighbour > matrix[row][col] for neighbour in neighbours): 
           low_point_coords.append([row, col])
    return low_point_coords

def get_valid_neighbours(matrix, row, col, max_row, max_col, discovered):
    neighbours = set()
    for i in list(range(4)):
        i_row = row + dirs['row'][i]
        i_col = col + dirs['col'][i]
        if 0 <= i_row <= max_row and 0 <= i_col <= max_col \
            and (i_row, i_col) not in discovered \
            and matrix[i_row][i_col] != 9:
            neighbours.add((i_row, i_col))
    return neighbours

def get_basin(matrix, row, col, max_row, max_col, discovered):
    discovered.add((row, col))
    valid_neighbours = get_valid_neighbours(matrix, row, col, max_row, max_col, discovered)
    if len(valid_neighbours) < 1:
        return discovered
    # no need to check if neighbours are actually increasing
    for n_coord in valid_neighbours:
        discovered.union(get_basin(matrix, n_coord[0], n_coord[1], max_row, max_col, discovered))
    return discovered

def get_all_basins(matrix):
    ROW, COL = len(matrix), len(matrix[0])
    basin_sizes = []
    low_point_coords = get_low_point_coord(matrix, ROW, COL)
    for n_coord in low_point_coords:
        discovered = set()
        local_basin = get_basin(matrix, n_coord[0], n_coord[1], ROW - 1, COL - 1, discovered)
        basin_sizes.append(len(local_basin))
    return basin_sizes

def get_prod_max_basins(matrix):
    basin_sizes = get_all_basins(matrix)
    basin_sizes = sorted(basin_sizes, reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

print("PART 2:", get_prod_max_basins(numbers))
