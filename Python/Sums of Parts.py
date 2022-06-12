"""
https://www.codewars.com/kata/5ce399e0047a45001c853c2b
"""


def parts_sums(ls):
    if len(ls) == 0:
        return [0]
    output = []
    suma = sum(ls)
    for x in range(len(ls)):
        output.append(suma)
        suma -= ls[x]
    output.append(0)
    return output
