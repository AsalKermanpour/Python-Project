#Asal kermanpour- Electrical ENgineering student in Kharazmi University- 4012061035

def Collatz_con(n):
    """
(int) -> int
in this function, you will recieve the result step of this evaluation:
if n=even -> n=n/2
if n=odd -> n=n*3+1
"""
    counter = 1
    while n != 1:
        if n % 2 ==0:
            n = n / 2
        else:
            n = n * 3 + 1
        if n == 1:
            break
        counter += 1
    return counter

n=int(input("please enter your number:"))
print("the step of this number will be:", Collatz_con(n))

        
