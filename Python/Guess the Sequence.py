"""
https://www.codewars.com/kata/5b45e4b3f41dd36bf9000090

You have read the title: you must guess a sequence. It will have something to do with the number given.
"""


def sequence(x):
    list = []
    for x in range(1, x + 1):
        list.append(x)
    list.sort(key=str)
    return list
