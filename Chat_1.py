username = input("Enter your name : ")
print("Welcome",username)

msg = input("Enter your message : ")
if msg == "hello":
    print("Hello",username)
elif msg == "bye":
    print("Bye",username,"See you soon")
else:
    print("I don't understand")
