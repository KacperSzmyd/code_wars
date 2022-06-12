"""
https://www.codewars.com/kata/59a1ea8b70e25ef8e3002992
"""


def describe_the_shape(angles):
    if angles <=2:
        return 'this will be a line segment or a dot'
    return 'This shape has {} sides and each angle measures {}'.format(angles, int((angles-2)*180/angles))