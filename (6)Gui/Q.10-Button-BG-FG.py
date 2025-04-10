import tkinter
from tkinter import *

def printHello():
    print("Hello World!")
window = Tk()

Button(window , text = " red" , fg="white",bg="red",command=printHello).pack()
Button(window , text = " blue" , fg="white",bg="blue",command=printHello).pack()
Button(window , text = " green" , fg="white",bg="green",command=printHello).pack()
Button(window , text = " yellow" , fg="white",bg="yellow",command=printHello).pack()


window.mainloop()
