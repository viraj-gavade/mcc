#to implement font colour and size - label
import tkinter as tk
root = tk.Tk()
tk.Label(root,text="use of font color",fg="blue",font="Times").pack()
tk.Label(root,text="use of font color",fg="light green", bg= "dark green",font="Helvetica 16 bold italic").pack()
tk.Label(root,text="Bold font style",fg="purple",bg="yellow",font="verdena 10 bold").pack()
root.mainloop()


