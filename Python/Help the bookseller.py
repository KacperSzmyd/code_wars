'''
https://www.codewars.com/kata/54dc6f5a224c26032800005c
'''


def stock_list(list_of_art, list_of_cat):
    checking_var = 0
    output = ""
    temp_books = 0
    if list_of_cat == "":
        return list_of_cat

    iter = 0

    for char in list_of_cat:
        for item in list_of_art:
            if item[0] == char:
                temp_books += int(item.split(" ")[1])
                checking_var += temp_books
        output += "({} : {})".format(char, temp_books)
        temp_books = 0

        iter += 1

        if iter < len(list_of_cat):
            output += " - "
    if checking_var == 0:
        return ""

    else:
        return output
