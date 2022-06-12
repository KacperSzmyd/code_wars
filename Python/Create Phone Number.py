"""
https://www.codewars.com/kata/525f50e3b73515a6db000b83

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in
the form of a phone number. """


def create_phone_number(n):
    phone = ""
    for x in range(len(n)):
        phone += str(n[x])
    return f"({phone[0]}{phone[1]}{phone[2]}) {phone[3]}{phone[4]}{phone[5]}-{phone[6]}{phone[7]}{phone[8]}{phone[9]}"
