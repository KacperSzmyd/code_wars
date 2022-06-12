'''
https://www.codewars.com/kata/57eb8fcdf670e99d9b000272

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''

def high(x):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    words = x.split(" ")
    winner = words[0]
    win_points = 0
    for word in words:
        points = 0
        for char in word:
            for x in range(len(alphabet)):
                if char == alphabet[x]:
                    points += x+ 1
                    break
                else:
                    continue
        if points > win_points:
            win_points = points
            winner = word

    return winner