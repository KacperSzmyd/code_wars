"""
https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if
that character appears only once in the original string, or ")" if that character appears more than once in the
original string. Ignore capitalization when determining if a character is a duplicate. """


def duplicate_encode(word):
    lower_word = word.lower()
    output = ""
    for x in range(len(word)):
        test = 1
        char = lower_word[x]
        for y in range(len(word)):
            if char == lower_word[y] and x != y:
                test = 0
        if test == 1:
            output += "("
        else:
            output += ")"
    return output
