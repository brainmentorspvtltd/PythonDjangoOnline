username = input("Enter your name : ")
print("Welcome",username)

#Logical Operators - and, or, not

msg = input("Enter your message : ")
if msg == "hello" or msg == "hey" or msg == "hi":
    print("Hello",username)
elif msg == "bye":
    print("Bye",username,"See you soon")
else:
    print("I don't understand")
