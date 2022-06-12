'''
https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4

Task Given an array of numbers and an index, return either the index of the smallest number that is larger than the
element at the given index, or -1 if there is no such index ( or, where applicable, Nothing or a similarly empty
value ).

Notes
Multiple correct answers may be possible. In this case, return any one of them.
The given index will be inside the given array.
The given array will, therefore, never be empty.
'''


def least_larger(a, i):
    b = [x for x in a if x > a[i]]
    if len(b) == 0:
        return -1
    return a.index(min(b))
