"""
https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

Count the number of Duplicates Write a function that will return the count of distinct case-insensitive alphabetic
characters and numeric digits that occur more than once in the input string. The input string can be assumed to
contain only alphabets (both uppercase and lowercase) and numeric digits. """


def duplicate_count(text):
    lowered = text.lower()
    used = ""
    output = 0
    for char in lowered:
        if lowered.count(char) >= 2 and char not in used:
            output += 1
            used += char
    return output
