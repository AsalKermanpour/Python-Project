def dayweek(n):
    '''
(integar) -> string
in this function, when you give an integar number, you will recieve the day of the week.
-----
n : integar
the integar number
return day
-----
'''
    if 1<=n<=7:
        if n == 1:
            return ("Saturday")
        elif n ==2:
            return ("Sunday")
        elif n == 3:
            return ("Monday")
        elif n == 4:
            return ("Tuesday")
        elif n == 5:
            return ("Wednesday")
        elif n == 6:
            return ("Thursday")
        else:
            return ("Friday")
    else:
        return ("ERROR")

n=int(input("enter the number:"))
print("the day of the week is:", dayweek(n))
