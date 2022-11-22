#Asal Kermanpour, Electrical Engineering in Kharazmi university, 4012061035
def Multi_division(a, b, c):
    """
(int, int, int) -> bool
in this function, it works like this:
Add a to itself b times
check if the result is divisible by c
examples:
EX3_4 (5, 2, 1) -> True
EX3_4 (1, 2, 3) -> False
"""
    while b != 0:
        d = a + a
        b -= 1
        if d % c == 0:
            return True
        else:
            return False

a=int(input("please enter the first number(a):"))
b=int(input("please enter the second number(b):"))
c=int(input("please enter the third number(c):"))
print("the answer of this compound is:", Multi_division(a, b, c))


        
