"""
https://www.codewars.com/kata/52f787eb172a8b4ae1000a34

Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...
"""


def zeros(n):
    number = 0
    while n // 5 >= 1:
        number += n // 5
        n = n // 5
    return number
