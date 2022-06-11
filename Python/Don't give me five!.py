'''https://www.codewars.com/kata/5813d19765d81c592200001a

In this kata you get the start number and the end number of a region and should
return the count of all numbers except numbers with a 5 in it.
The start and the end number are both inclusive!
'''

def dont_give_me_five(start,end):
    numbers_without_fives = [str(num) for num in range(start,end+1) if not '5' in str(num)]
    return len(numbers_without_fives)