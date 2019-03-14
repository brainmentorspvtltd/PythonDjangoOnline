x = 12
y = 34
def add():
    #Local Variables
    x = 10
    #y = 23
    global z
    z = x + y
    print(z)

add()
print("Outside function",z)
