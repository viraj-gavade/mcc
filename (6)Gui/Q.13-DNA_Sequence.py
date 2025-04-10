
#counting DNA Sequence letter
import tkinter as tk
def count_bases():
    seq=entry.get().upper()
    result.set(f"A:{seq.count('A')}T:{seq.count('T')}C:{seq.count('C')}G:{seq.count('G')}")
root=tk.Tk()
entry=tk.Entry(root)
entry.pack()
result=tk.StringVar()
tk.Button(root,text="count",command=count_bases).pack()
tk.Label(root,textvariable=result).pack()
root.mainloop()
