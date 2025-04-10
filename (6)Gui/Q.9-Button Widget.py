#button widget Q-9
from tkinter import *
from tkinter import messagebox
top = Tk()

def helloCallBack():
    messagebox.showinfo("Hello Python","Good Morning")

b = Button(top,text="Hello",command = helloCallBack)


b.pack()
top.mainloop()
