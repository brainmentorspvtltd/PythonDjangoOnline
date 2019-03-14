def add(x,y):
    z = x + y
    print(z)
def sub(x,y):
    z = x - y if x > y else y - x
    print(z)
def div(x,y):
    z = x / y
    print(z)

def errHandler(*args):
    print("Invalid Choice...")

print("""
1. Add
2. Sub
3. Div
4. Mul
""")
choice = input("Enter your choice : ")
num_1 = int(input("Enter first number : "))
num_2 = int(input("Enter second number : "))
operations = {
    "1":add,
    "2":sub,
    "3":div
    }
operations.get(choice, errHandler)(num_1, num_2)
