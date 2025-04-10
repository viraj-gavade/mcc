import tkinter
from tkinter import *
def submit():
  if(var1.get()=="abc")&(var2.get()=="123"):
    print("Welcome",var1.get())
root=Tk()
var1=StringVar()
var2=StringVar()
L1=Label(root,text="USERNAME:").grid(row=1,column=0)
#L1.pack()
e1=Entry(root,textvariable=var1).grid(row=1,column=1)
#e1.pack()
L2=Label(root,text="PASSWORD").grid(row=2,column=0)
#L2.pack()
e2=Entry(root,textvariable=var2,show="*").grid(row=2,column=1)
#e2.pack()
b1=Button(root,text="SUBMIT",command=submit).grid(row=3,column=0)
b2=Button(root,text="CANCEL",command=quit).grid(row=3,column=1)
#b1.pack()
root.mainloop()
