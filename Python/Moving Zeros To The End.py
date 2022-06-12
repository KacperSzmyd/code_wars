"""
https://www.codewars.com/kata/52597aa56021e91c93000cb0

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
"""


def move_zeros(array):
    count = array.count(0)
    output = []
    for x in range(len(array)):
        if array[x] != 0:
            output.append(array[x])
    for x in range(count):
        output.append(0)

    return output