'''
https://www.codewars.com/kata/586d6cefbcc21eed7a001155


'''


def longest_repetition(chars):
    output = ["", 0]

    if len(chars) == 0:
        return tuple(output)

    letter = chars[0]
    instances = 1
    iter = 1

    for char in chars:
        temp_inst = 1
        for x in range(iter, len(chars)):
            if chars[x] == char:
                temp_inst += 1
            else:
                break
        if temp_inst > instances:
            instances = temp_inst
            letter = char
        iter += 1

    output[0] = letter
    output[1] = instances

    return tuple(output)
