import tkinter
from tkinter import *
def increment(text):
    count = int(text.get())
    text.set(str(count+1))

window = tkinter.Tk()
frame = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
text = tkinter.StringVar()
text.set('0')
button = tkinter.Button(frame,textvar=text,command = lambda:increment(text))
button.pack()
window.mainloop()
