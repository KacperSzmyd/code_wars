"""
https://www.codewars.com/kata/5865cff66b5699883f0001aa

All Star Code Challenge #22

Create a function that takes an integer argument of seconds and converts the value into a string describing how many
hours and minutes comprise that many seconds.

Any remaining seconds left over are ignored.

Note:
The string output needs to be in the specific form - "X hour(s) and X minute(s)"
"""


def to_time(seconds):
    return f"{seconds // 3600} hour(s) and {seconds % 3600 // 60} minute(s)"
