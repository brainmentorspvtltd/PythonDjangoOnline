def outer():
    x = 10
    y = 34
    def inner_1():
        z = x + y
        return z
    def inner_2():
        z = x - y
        return z
    
    #print(inner_1())
    #print(inner_2())
    return inner_1, inner_2
    
add,sub = outer()
#print(add())
#print(sub())

print(outer()[0]())
