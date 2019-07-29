#importing modules
from tkinter import *
import sqlite3

class Assistant:
    master = Tk()
    #defining title and size of window
    master.title("Welcome my aka")
    master.minsize(320,320)
    master.geometry('640x480')

    # creating user name field
    userNameLabel = Label(master, text="User Name")
    userNameLabel.grid(column=0,row=0)
    usertxt = Entry(master, width=20)
    usertxt.grid(column=1, row=0)

    #creating password field
    passwordLabel = Label(master, text="Password")
    passwordLabel.grid(column=0,row=1)
    passwordtxt = Entry(master, width=20)
    passwordtxt.grid(column=1, row=1)

    #creating login Button
    loginbtn = Button(master, text="login", command = lambda: validateUser(usertxt,passwordtxt))
    loginbtn.grid(column=2, row=2)
