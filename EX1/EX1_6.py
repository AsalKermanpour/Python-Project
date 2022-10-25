def romannum(n):
    '''
(integar) -> string
in this function, when you give a number, you will recieve the Romanisation of that number.
------
for example:
>>> n = 4
IV
-----
'''
    if n == 1:
        return ("I")
    elif n == 2:
        return ("II")
    elif n == 3:
        return ("III")
    elif n == 4:
        return ("IV")
    elif n ==5:
        return ("V")
    elif n == 6:
        return ("VI")
    elif n == 7:
        return ("VII")
    elif n == 8:
        return ("VIII")
    elif n == 9:
        return ("IX")
    elif n == 10:
        return ("X")
    else:
        return ("ERROR")

n=int(input(" enter your number:"))
print("the Romanisation of your number is:", romannum(n))

      
