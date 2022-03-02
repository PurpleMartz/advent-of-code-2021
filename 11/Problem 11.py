# -*- coding: utf-8 -*-
"""
@author: PurpleMartz
"""

from itertools import product

data = open("Problem 11 Data.txt", "r").read()

data = data[:-1].split('\n')
data = [[int(n) for n in row] for row in data]
dirs = {'row': [-1, -1, -1, 0, 0, 1, 1, 1], 'col': [-1, 0, 1, -1, 1, -1, 0, 1]}

def increase_energy_lvls(grid):
    return [[n + 1 for n in row] for row in grid]

def normalise_energy_lvls(grid):
    return [[0 if n > 9 else n for n in row] for row in grid]

def flash(grid, row, col, max_row, max_col, flashed):
    if (row, col) in flashed:
        return grid
    flashed.add((row, col))
    for i in list(range(8)):
        i_row = row + dirs['row'][i]
        i_col = col + dirs['col'][i]
        if 0 <= i_row <= max_row and 0 <= i_col <= max_col:
            grid[i_row][i_col] += 1
            if grid[i_row][i_col] > 9:
                grid = flash(grid, i_row, i_col, max_row, max_col, flashed)
    return grid      

def calc_flashes(grid, steps):
    flashes_count = 0
    ROW, COL = len(grid), len(grid[0])
    for step in range(steps):
        grid = increase_energy_lvls(grid)
        flashed = set()
        for row, col in product(range(ROW), range(COL)):
            if (row, col) in flashed or grid[row][col] <= 9:
                continue
            grid = flash(grid, row, col, ROW - 1, COL - 1, flashed)
        grid = normalise_energy_lvls(grid)
        flashes_count += len(flashed)
    return flashes_count, grid

def check_correctness():
    grid = open("Problem 11 Test Input.txt", "r").read()    
    grid = grid[:-1].split('\n')
    grid = [[int(n) for n in row] for row in grid]
    
    expected_answer_grid = open("Problem 11 Test Output.txt", "r").read()
    expected_answer_grid = expected_answer_grid[:-1].split('\n')
    expected_answer_grid = [[int(n) for n in row] for row in expected_answer_grid]
    expected_answer_flashes = 204
    
    real_answer = calc_flashes(grid, 10)
    
    assert real_answer[1] == expected_answer_grid
    assert real_answer[0] == expected_answer_flashes

print("PART 1:", calc_flashes(data, 100)[0])

def get_ultimate_step(grid, steps):
    ROW, COL = len(grid), len(grid[0])
    SIZE = ROW * COL
    for step in range(steps):
        grid = increase_energy_lvls(grid)
        flashed = set()
        for row, col in product(range(ROW), range(COL)):
            if (row, col) in flashed or grid[row][col] <= 9:
                continue
            grid = flash(grid, row, col, ROW - 1, COL - 1, flashed)
        grid = normalise_energy_lvls(grid)
        if(len(flashed) == SIZE):
            return step + 1
    return steps

# Don't wanna lock my machine into an infinite loop :D
print("PART 2:", get_ultimate_step(data, 10000))
