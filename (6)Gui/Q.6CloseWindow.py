#click on good bye button
import tkinter
from tkinter import *
window=tkinter.Tk()
frame=tkinter.Tk()
frame=tkinter.Frame(window)
frame.pack()
button = tkinter.Button(frame , text="GOOD BYE",command=lambda:window.destroy())
button.pack()
window.mainloop()
