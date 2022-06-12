"""
https://www.codewars.com/kata/54da5a58ea159efa38000836

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""


def find_it(seq):
    for x in range(len(seq)):
        counter = 0
        number = seq[x]
        for y in range(len(seq)):
            if seq[y] == number:
                counter += 1
        if counter % 2 == 1:
            return number
