# -*- coding: utf-8 -*-
"""
@author: PurpleMartz
"""

from collections import Counter

data = open("Problem 06 Data.txt", "r").read()
"""
data = '''3,4,3,1,2
'''
"""

data = data[:-1].split(',')
existing_fish = dict(Counter(data))
existing_fish = {int(key): value for key, value in existing_fish.items()}

all_fish = dict()
for i in range(9):
    all_fish[i] = 0

all_fish = {**all_fish, **existing_fish}
all_fish_copy = all_fish.copy()

for day in range(80):
    temp = all_fish[0]
    for i in range(8):
        all_fish[i] = all_fish[i + 1]
    all_fish[8] = temp
    all_fish[6] += temp

print("PART 1:", sum(all_fish.values()))

all_fish = all_fish_copy.copy()

for day in range(256):
    temp = all_fish[0]
    for i in range(8):
        all_fish[i] = all_fish[i + 1]
    all_fish[8] = temp
    all_fish[6] += temp

print("PART 2:", sum(all_fish.values()))