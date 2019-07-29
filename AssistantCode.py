#importing modules
from tkinter import *
import sqlite3
from gtts import gTTS
from playsound import playsound

class Assistant:

    greetings = "Hi I'm Jarvis. \nPlease confirm your identity..."

    def __init__(self,frame):
        #defining title and size of window
        frame.title("Welcome my aka")
        frame.minsize(320,320)
        frame.geometry('640x480')

        #creating greeting string
        self.greetingLabel = Label(frame, text=Assistant.greetings, fg = "blue", bg="black", font = "monospace 20").pack()

        # creating user name field
        self.userNameLabel = Label(frame, text="User Name")
        self.userNameLabel.place(x=70,y=100)
        self.usertxt = Entry(frame, width=20)
        self.usertxt.place(x=200,y=100)

        #creating password field
        self.passwordLabel = Label(frame, text="Password")
        self.passwordLabel.place(x=70,y=150)
        self.passwordtxt = Entry(frame, width=20)
        self.passwordtxt.place(x=200,y=150)

        #creating login Button
        self.loginbtn = Button(frame, text="login", command = "something")
        self.loginbtn.place(x=150,y=200)

    def greet(self):
        # run audio
        gttsGreetings = gTTS(text=Assistant.greetings,lang='en',slow=False).save("greeting.mp3")
        playsound("greeting.mp3")

window = Tk()
x = Assistant(window)
x.greet()
window.mainloop()
