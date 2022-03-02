# -*- coding: utf-8 -*-
"""
@author: PurpleMartz
"""

data = open("Problem 10 Data.txt", "r").read()
"""
data = '''[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''
"""

data = data[:-1].split('\n')
opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']

def get_symbol_balances(rows):
    symbol_balances = [0, 0, 0, 0]
    for row in rows:
        symbol_stack = []
        for symbol in row:
            if symbol in opening:
                symbol_stack.append(symbol)
            else:
                index = closing.index(symbol)
                if len(symbol_stack) > 0:
                    nearest_opening_symbol = symbol_stack.pop()
                    if nearest_opening_symbol == opening[index]:
                        continue
                symbol_balances[index] += 1
                break
    return symbol_balances

def calc_syntax_error_score(data):
    balances = get_symbol_balances(data)
    return balances[0] * 3 + balances[1] * 57 + balances[2] * 1197 + balances[3] * 25137

print("PART 1:", calc_syntax_error_score(data))

symbol_points = {')': 1, ']': 2, '}': 3, '>': 4}
def calc_autocompletion_score(completion_string):
    score = 0
    for symbol in completion_string:
        score *= 5
        score += symbol_points[symbol]
    return score

def get_middle_score(scores):
    scores = sorted(scores)
    size = len(scores)
    return scores[int((size - 1)/2)]

def build_phrase(remaining_symbol_stack):
    completion_string = ''
    for symbol in remaining_symbol_stack:
        index = opening.index(symbol)
        completion_string = closing[index] + completion_string
    return completion_string

def get_score(rows):
    scores = []
    for row in rows:
        symbol_stack = []
        valid = True
        for symbol in row:
            if symbol in opening:
                symbol_stack.append(symbol)
            else:
                index = closing.index(symbol)
                if len(symbol_stack) > 0:
                    nearest_opening_symbol = symbol_stack.pop()
                    if nearest_opening_symbol == opening[index]:
                        continue
                valid = False
                break
        if valid and len(symbol_stack) > 0:
            completion_string = build_phrase(symbol_stack)
            score = calc_autocompletion_score(completion_string)
            scores.append(score)
    return get_middle_score(scores)

print("PART 2:", get_score(data))
