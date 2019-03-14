from datetime import datetime
import webbrowser
import os, random

username = input("Enter your name : ")
print("Welcome",username)

helloIntent = ["hello","hi","hey","howdy","hey there","hi there","hello there"]

timeIntent = ["tell me time","time please","what's the time","time","current time"]
dateIntent = ["tell me date","date please","what's the date today","today's date"]

chat = True
while chat:
    msg = input("Enter your message : ")
    if msg in helloIntent:
        print("Hello",username)
    elif msg in timeIntent:
        t = datetime.now().time()
        print(t.strftime("%H:%M:%S, %p"))
    elif msg in dateIntent:
        d = datetime.now().date()
        print(d.strftime("%d/%m/%y, %a"))
    elif msg.startswith("open"):
        web = msg.split()[-1]
        webbrowser.open(web+'.com')
    elif msg == "play music":
        os.chdir(r"C:\Users\asus\Videos\Movavi Video Editor\Media Content\Audio")
        songs = os.listdir()
        s = random.choice(songs)
        os.startfile(s)
    elif msg == "bye":
        print("Bye",username,"See you soon")
        chat = False
    else:
        print("I don't understand")
