from tkinter import *
def sq ():
  n=int(e_no.get())
  m=n*n
  l_display.config(text=m)
root=Tk()
f1=Frame()
f1.pack()

l_no=Label(f1,text="Enter a number")
l_no.pack()

e_no=Entry(f1)
e_no.pack()

l_result=Label(f1,text="Result")
l_result.pack()

l_display=Label(f1,text="")
l_display.pack()

b_square=Button(f1,text="SQUARE",command=sq)
b_square.pack(side=LEFT)

b_quit=Button(f1,text="Quit",command=quit)
b_quit.pack(side=RIGHT)
root.mainloop()
