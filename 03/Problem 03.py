# -*- coding: utf-8 -*-
"""
@author: PurpleMartz
"""

data = open("Problem 03 Data.txt", "r").read()
data = data[:-1].split('\n')

n_digits = len(data[0])
digit_balance = {i: 0 for i in range(n_digits)}

for number in data:
    for i in range(n_digits):
        digit = number[i]
        if digit == '1':
            digit_balance[i] += 1
        else:
            digit_balance[i] -= 1

gamma_rate = ''
epsilon_rate = ''
for i in range(n_digits):
    if digit_balance[i] > 0:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'
print("PART 1:", int(gamma_rate, 2) * int(epsilon_rate, 2))


def get_rating(numbers, prefix, is_o2 = True):
    # If we reduced the number of valid numbers down to 1, return.
    if len(numbers) <= 1:
        return numbers[0]
    
    # Count occurences of bits.
    digit_balance = 0
    for number in numbers:
        digit = number[len(prefix)]
        if digit == '1':
            digit_balance += 1
        else:
            digit_balance -= 1
    
    # Find the valid prefix.
    if is_o2:
        prefix += '0' if digit_balance < 0 else '1'
    else:
        prefix += '1' if digit_balance < 0 else '0'
    
    new_numbers = [x for x in numbers if x.startswith(prefix)] 
    return get_rating(new_numbers, prefix, is_o2)

o2_rating = get_rating(data, '', True)
co2_rating = get_rating(data, '', False)
print("PART 2:", int(o2_rating, 2) * int(co2_rating, 2))
