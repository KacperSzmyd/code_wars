"""
https://www.codewars.com/kata/602afedfd4a64d0008eb4e6e

What date corresponds to the nth day of the year?
The answer depends on whether the year is a leap year or not.

Write a function that will help you determine the date if you know the number of the day in the year, as well as
whether the year is a leap year or not. The function accepts the day number and a boolean value isLeap as arguments,
and returns the corresponding date of the year as a string "Month, day". Only valid combinations of a day number and
isLeap will be tested. """

def get_day(days, is_leap):
    calendar = {
        "January": 31,
        "February": 28+(1 if is_leap else 0),
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
      }
    for month in calendar:
        if days <= calendar[month]:
            return f'{month}, {days}'
        days -= calendar[month]