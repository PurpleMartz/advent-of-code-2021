# -*- coding: utf-8 -*-
"""
@author: PurpleMartz
"""
import re

data = open("Problem 04 Data.txt", "r").read()
"""
data = '''7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''
"""

calls, *cards_original = data[:-1].split('\n\n')
calls = calls.split(',')
cards_original = [card + '\n' for card in cards_original]
cards = cards_original.copy()

# Exercising crazy regex ^^
bingo_column = r'X(\s+)([0-9]+|X)(\s+)([0-9]+|X)(\s+)([0-9]+|X)(\s+)([0-9]+|X)(\s+)X(\s+)([0-9]+|X)(\s+)([0-9]+|X)(\s+)([0-9]+|X)(\s+)([0-9]+|X)(\s+)X(\s+)([0-9]+|X)(\s+)([0-9]+|X)(\s+)([0-9]+|X)(\s+)([0-9]+|X)(\s+)X(\s+)([0-9]+|X)(\s+)([0-9]+|X)(\s+)([0-9]+|X)(\s+)([0-9]+|X)(\s+)X'
bingo_row = r'X X X X X'

def is_bingo(card):
    if re.search(bingo_row, card) or re.search(bingo_column, card):
        return True
    return False

def update_card(card, call):
    call = call.rjust(2)
    return card.replace(f'{call} ', 'X ').replace(f'{call}\n', 'X\n')

def get_winner(calls, cards):
    for call in calls:
        for i in range(len(cards)):
            cards[i] = update_card(cards[i], call)
            if is_bingo(cards[i]):
                return call, cards[i]

def unmarked_numbers_sum(card):
    unmarked_numbers = re.findall(r'\d+', card)
    unmarked_numbers = list(map(int, unmarked_numbers))
    return sum(unmarked_numbers)

winner_call, winner_card = get_winner(calls, cards)
print("PART 1:", int(winner_call) * unmarked_numbers_sum(winner_card))

cards = cards_original.copy()

def get_loser(calls, cards):
    losers = list(range(len(cards)))
    for call in calls:
        losers_copy = losers.copy()
        for i in losers_copy:
            cards[i] = update_card(cards[i], call)
            if is_bingo(cards[i]):
                losers.remove(i)
            if len(losers) <= 0:
                return call, cards[i]

loser_call, loser_card = get_loser(calls, cards)
print("PART 2:", int(loser_call) * unmarked_numbers_sum(loser_card))

# Much better, re-implement: https://www.codespeedy.com/create-bingo-game-using-python/
