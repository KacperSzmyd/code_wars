'''
https://www.codewars.com/kata/523f5d21c841566fde000009
'''


def array_diff(a, b):
    output = []
    for x in a:
        if x in b:
            continue
        else:
            output.append(x)

    return output