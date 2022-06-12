"""
https://www.codewars.com/kata/567501aec64b81e252000003
"""

import math


def wallpaper(l, w, h):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
               "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    if l == 0 or w == 0 or h == 0:
        return numbers[0]
    m2 = 2 * (w * h) + 2 * (l * h)
    to_buy = m2 * 1.15
    rolls = 0.52 * 10
    output = math.ceil(to_buy / rolls)
    return numbers[output]
