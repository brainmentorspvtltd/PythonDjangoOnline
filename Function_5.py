#Decorators - Passing function as an argument in a function

def show(func):
    print(func())

@show
def sayHello():
    return "Hello User"

@show
def sayBye():
    return "Bye User"

#show(sayBye)
#show(sayHello)
