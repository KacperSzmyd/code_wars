'''https://www.codewars.com/kata/5254ca2719453dcc0b00027d

In this kata you have to create all permutations of a non empty input string
and remove duplicates, if present. This means, you have to shuffle all letters
from the input in all possible orders.'''


from itertools import permutations as pr


def permutations(string):
    sorted_permutation_without_repetitions = set(pr(string))
    output = []

    for item in sorted_permutation_without_repetitions:
        output.append(''.join(item))

    return output
