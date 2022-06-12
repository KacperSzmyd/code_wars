'''
https://www.codewars.com/kata/5966eeb31b229e44eb00007a

ASC Week 1 Challenge 4 (Medium #1)

Write a function that converts any sentence into a V A P O R W A V E sentence. a V A P O R W A V E sentence converts
all the letters into uppercase, and adds 2 spaces between each letter (or special character) to create this V A P O R
W A V E effect.

Note that spaces should be ignored in this case.
'''


def vaporcode(s):
    return (''.join(list(map(lambda x: x.upper() + ' ' if x != ' ' else '', s)))).strip()
