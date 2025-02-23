from tkinter import *
import requests
import time 

status = 0

def GUI():
    guiWin = Tk()
    guiWin.title('DedJokes(TestBuild 0.3.2).exe')
    whitespace1 = Label(guiWin , text='---------------------------------------------------------------')
    whitespace1.pack()
    actvTxt = Label(guiWin , text='Activate DadJokes.exe')
    actvTxt.pack()
    whitespace2 = Label(guiWin , text='  ')
    whitespace2.pack()
    enblBtn = Button(guiWin , text='Click Me!', command= ActDact())
    enblBtn.pack()
    whitespace3 = Label(guiWin , text='---------------------------------------------------------------')
    whitespace3.pack()
    guiWin.mainloop()

def ActDact():
    global status
    if status == 0:
        status = 1
    else:
        status = 0

def GetJoke():
    jokeWin = Tk()
    jokeWin.title('Your Joke!')
    jokeWid = Label(jokeWin , text = requests.get("https://v2.jokeapi.dev/joke/Any?lang=en&format=txt&type=double").text)
    jokeWid.pack()
    jokeWin.mainloop()

def JokeLoop():
    global status
    while status == 1:
        GetJoke()
        time.sleep(3)
GUI()
JokeLoop()