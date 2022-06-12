'''
https://www.codewars.com/kata/569d488d61b812a0f7000015


'''

def data_reverse(data):
    output = []
    lst = [data[x: x +8] for x in range(0 ,len(data) ,8)]
    rev_list = lst[::-1]
    for x in rev_list:
        output += x

    return output