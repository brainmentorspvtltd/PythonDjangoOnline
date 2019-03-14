'''
def calc(x,y):
    z = x + y
    return z
'''

def calc(x,y):
    return x+y, x-y, x/y, x*y

#print(calc(4,5))
x = calc(4,5)
print(x)


#Packing and Unpacking in python
a,b,c,d = calc(4,5)
print(a,b,c,d)

a,b,*c = calc(4,5)
print(a,b,c)
