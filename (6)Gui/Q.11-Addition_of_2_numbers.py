import tkinter
from tkinter import *
def add():
  n=7+8
  label.config(text=n)
  print("addition is ",n)
root=Tk()
f1=Frame()
f1.pack()
label=Label(root,text="")
label.pack()
b_add=Button(f1,text="ADD",command=add)
b_add.pack(side=RIGHT)
b_quit=Button(f1,text="quit",command=quit)
b_quit.pack(side=LEFT)
root.mainloop()
