def maxedge(a,b):
   '''
(integar),(integar) -> integar
this function, will give you the maximum edge of the triangle by give it the other edges.
--------
a : integar
one of the edges
b : integar
rhe other edge
c : integar
the maximum edge
 if (a+b>c) and if (a+c>b) and if (b+c>a):
    print("the triangle is correct")
    c=(a+b)-1
    return c
else:
print("error")
--------
'''
   c=(a+b)-1
   return c

a=int(input("enter the first edge:"))
b=int(input("enter the second edge:"))
if a<=0 or b<=0:
    print("ERROR")
else:
    print("the third and the maximum edge of the triangle is:", maxedge(a,b))
    
  
