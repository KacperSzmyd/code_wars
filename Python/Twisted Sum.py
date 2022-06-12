"""
https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f

Find the sum of the digits of all the numbers from 1 to N (both ends included).
"""


def compute_sum(n):
    number = ""
    output = 0
    for x in range(1, n + 1):
        number += str(x)

    for char in number:
        output += int(char)
    return output