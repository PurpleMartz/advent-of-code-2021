# -*- coding: utf-8 -*-
"""
@author: PurpleMartz
"""

from collections import defaultdict

data = open("Problem 12 Data.txt", "r").read()

def parse_graph(data):
    data = data[:-1].split('\n')
    # checking belonging to set is quicker than that to list - O(1) vs O(n)
    graph = defaultdict(list)
    for row in data:
        cave_1, cave_2 = row.split('-')
        graph[cave_1].append(cave_2)
        graph[cave_2].append(cave_1)
    return graph

def print_all_paths_util(graph, start, destination, visited, path, all_paths):
    if start.islower():
        visited.add(start)
    path.append(start)

    if start == destination:
        all_paths.append(path.copy())
    else:
        for i in graph[start]:
            if i not in visited:
                print_all_paths_util(graph, i, destination, visited, path, all_paths)
       
    if start.islower():
        visited.remove(start)
    path.pop()

def print_all_paths(graph, start, destination):
    visited = set()
    all_paths = []
    path = []
 
    print_all_paths_util(graph, start, destination, visited, path, all_paths)
    return all_paths

def parse_answer(answer):
    answer = answer[:-1].split('\n')
    answer = [row.split(',') for row in answer]
    return answer

def check_correctness():
    graph = open("Problem 12 Test Input.txt", "r").read()
    graph = parse_graph(graph)
    all_paths = print_all_paths(graph, 'start', 'end')
    answer = open("Problem 12 Test Output 1.txt", "r").read()
    answer = parse_answer(answer)
    assert set(map(tuple, answer)) == set(map(tuple,all_paths))
    
graph = parse_graph(data)
print("PART 1:", len(print_all_paths(graph, 'start', 'end')))


def print_all_paths_util_special(graph, start, destination, visited, path, all_paths, special_cave, special_cave_visited):
    if start.islower():
        if start != special_cave:
            visited.add(start)
        elif special_cave_visited > 0:
            visited.add(start)
            special_cave_visited += 1
        else:
            special_cave_visited += 1
    path.append(start)

    if start == destination:
        all_paths.add(tuple(path))
    else:
        for i in graph[start]:
            if i not in visited:
                print_all_paths_util_special(graph, i, destination, visited, path, all_paths, special_cave, special_cave_visited)
       
    if start.islower():
        if start != special_cave:
            visited.remove(start)
        elif special_cave_visited > 1:
            visited.remove(start)
            special_cave_visited -= 1
        else:
            special_cave_visited -= 1
    path.pop()

def print_all_paths_special(graph, start, destination):
    all_paths = set()
    lowercase_caves = [cave for cave in graph.keys() if cave.islower() and cave != 'start' and cave != 'end']
    
    for lowercase_cave in lowercase_caves:
        visited = set()
        path = []
        print_all_paths_util_special(graph, start, destination, visited, path, all_paths, lowercase_cave, 0)
    return all_paths

def check_correctness_special():
    graph = open("Problem 12 Test Input.txt", "r").read()
    graph = parse_graph(graph)
    all_paths = print_all_paths_special(graph, 'start', 'end')
    answer = open("Problem 12 Test Output 2.txt", "r").read()
    answer = parse_answer(answer)
    assert set(map(tuple, answer)) == all_paths

print("PART 2:", len(print_all_paths_special(graph, 'start', 'end')))

# Really not optimal - work on optimising the second one.