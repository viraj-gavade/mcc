#Listbox
from tkinter import *
top = Tk()
Lb = Listbox(top)
Lb.insert(1,"Python")
Lb.insert(2,"C")
Lb.insert(3,"C++")
Lb.insert(4,"JAVA")
Lb.insert(5,"Ruby")
Lb.pack()
top.mainloop()
