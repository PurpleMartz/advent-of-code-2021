# -*- coding: utf-8 -*-
"""
@author: PurpleMartz
"""

data = open("Problem 08 Data.txt", "r").read()
"""
data = '''be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''
"""

data = data[:-1].split('\n')

n_segments = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
accepted_n_segments = [n_segments[1], n_segments[4], n_segments[7], n_segments[8]]
counter = 0
for row in data:
    inputs, outputs = row.split(' | ')
    outputs = outputs.split(' ')
    for output in outputs:
        if len(output) in accepted_n_segments:
            counter += 1
            
print("PART 1:", counter)

def remove_elements(array, *elements):
    for element in elements:
        array.remove(element)

def decode_numbers(row_inputs):
    row_inputs = row_inputs.split(' ')
    row_inputs = [set(row_input) for row_input in row_inputs]
    for n in row_inputs:
        if len(n) == 2:
            n_1 = n
        if len(n) == 3:
            n_7 = n
        if len(n) == 4:
            n_4 = n
        if len(n) == 7:
            n_8 = n
    remove_elements(row_inputs, n_1, n_7, n_4, n_8)
    for n in row_inputs:
        if len(n.difference(n_1)) == 3:
            n_3 = n
        if len(n.difference(n_1)) == 5:
            n_6 = n
    n_9 = n_3.union(n_4)
    remove_elements(row_inputs, n_3, n_6, n_9)
    for n in row_inputs:
        if len(n.difference(n_9)) == 0:
            n_5 = n
    remove_elements(row_inputs, n_5)
    for n in row_inputs:
        if len(n) == 5:
            n_2 = n
        if len(n) == 6:
            n_0 = n
    remove_elements(row_inputs, n_2, n_0)
    return [n_0, n_1, n_2, n_3, n_4, n_5, n_6, n_7, n_8, n_9]

def construct_number(digit_array):
    number = 0
    power = len(digit_array) - 1
    for i in range(len(digit_array)):
        digit = digit_array[i]
        number += digit * pow(10, power - i)
    return number

def find_number(row):
    row_inputs, row_outputs = row.split(' | ')
    decoded = decode_numbers(row_inputs)
    row_outputs = row_outputs.split(' ')
    digit_array = [decoded.index(set(n)) for n in row_outputs]
    return construct_number(digit_array)

number_sum = 0
for row in data:
    number_sum += find_number(row)
            
print("PART 2:", number_sum)
    