'''https://www.codewars.com/kata/554b4ac871d6813a03000035

In this little assignment you are given a string of
space separated numbers, and have to return the highest and lowest number.'''


def high_and_low(numbers):
    num_list = [int(x) for x in numbers.split(' ')]
    return str(max(num_list)) + ' ' + str(min(num_list))