'''
https://www.codewars.com/kata/585d7d5adb20cf33cb000235

There is an array with some numbers. All numbers are equal except for one. Try to find it!
'''


def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b