# by default input will be of string type
name = input("Enter your name: ")
#msg = "Hello " + name
msg = "Hello {}".format(name)
print(msg)

# we have to type cast the data
num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))
result = num_1 + num_2
print(result)
