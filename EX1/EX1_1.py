def nextnumber(n):
    '''
(int) -> int
in this function, for the input, you will get an integar number. then you will get your output as the next number of that number.
you can see the way that this function workd:
    integar(output) = integar(input) + 1
    return integar(output)
    '''
    n+=1
    return n
n = int(input("enter your number:"))
nextnumber(n)
print (nextnumber(n))
