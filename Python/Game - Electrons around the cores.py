"""
https://www.codewars.com/kata/52210226578afb73bd0000f1

Have you heard of the game "electrons around the cores"? I'm not allowed to give you the complete rules of the game,
just so much:

the game is played with 4 to 6 dice, so you get an array of 4 to 6 numbers, each 1-6
the name of the game is important
you have to return the correct number five times in a row and your solution is considered to be correct
If you just press "submit", you'll get an array and the expected value!

Here are some input/output pairs for you to wrap your mind around:

[ 1, 2, 3, 4, 5 ] -> 6
[ 2, 2, 3, 3 ] -> 4
[ 6, 6, 4, 4, 1, 3 ] -> 2
[ 3, 5, 3, 5, 4, 2 ] -> 12
And yes, it is a shameless copy of a famous game.
"""

def electrons_around_the_cores(dice):
    sum = 0
    for x in dice:
        if x%2 != 0:
            sum += x-1
    return sum