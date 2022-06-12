'''https://www.codewars.com/kata/56a1c074f87bc2201200002e

Write a function that given, an array arr, returns an array
 containing at each index i the amount of numbers that are smaller than arr[i] to the right.
'''


def smaller(arr):
    output = []
    for x in range(len(arr)-1):
        counter = 0
        for y in range(x, len(arr)):
            if arr[y] < arr[x]:
                counter += 1
        output.append(counter)
    output.append(0)
    return output