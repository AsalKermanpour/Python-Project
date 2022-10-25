def ageclass(n):
    '''
(integar) -> string
in this function, when you give the age of a person, the output of this code will be the class of the age.
--------
for example:
>>>age(input) = 20
Adult
-------
'''
    if 0<n<=1:
        return ("Infant")
    elif 1<n<13:
        return ("Child")
    elif 13<=n<20:
        return ("Teenager")
    else:
        return ("Adult")

n=int(input("enter the age:"))
print("the class of this age is:", ageclass(n))
