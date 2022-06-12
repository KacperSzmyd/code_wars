"""
https://www.codewars.com/kata/5239f06d20eeab9deb00049b

The function 'fibonacci' should return an array of fibonacci numbers. The function takes a number as an argument to
decide how many no. of elements to produce. If the argument is less than or equal to 0 then return empty array """


def fibonacci(n):
    arr = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return arr
    else:
        for x in range(n - 2):
            arr.append(arr[x] + arr[x + 1])
        return arr
