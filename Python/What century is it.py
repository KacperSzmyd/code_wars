'''
https://www.codewars.com/kata/52fb87703c1351ebd200081f

Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.
'''

def what_century(year):
    numb = int(year)

    output = str((numb // 100)+1)

    if numb % 100 == 0:
        output = str((numb // 100))
    print(output[1], output[0])
    if output[1] == '1' and output[0] != '1':
        return output + "st"
    if output[1] == '2' and output[0] != '1':
        return output + "nd"
    if output[1] == '3' and output[0] != '1':
        return output + "rd"


    else:
        return output + 'th'