"""
https://www.codewars.com/kata/60908bc1d5811f0025474291

Complete the function that takes an odd integer (0 < n < 1000000) which is the difference between two consecutive
perfect squares, and return these squares as a string in the format "bigger-smaller" """


def find_squares(num):
    return "{}-{}".format((num // 2 + 1) ** 2, (num // 2) ** 2)
