#Menu
from tkinter import  *
root = Tk()
def doNothing():
    filewin=Toplevel(root)
    button = Button(filewin , text = "do nothing button")
    button.pack()

menubar = Menu(root)

fileMenu = Menu(menubar,tearoff=0)
fileMenu.add_command(label="New",command=doNothing)
fileMenu.add_command(label = "Open" , command=doNothing)
fileMenu.add_command(label = "Save" , command=doNothing)
fileMenu.add_command(label = "SaveAs" , command=doNothing)
fileMenu.add_command(label = "Close" , command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit" , command=root.quit)
menubar.add_cascade(label="FILE",menu=fileMenu)

editMenu = Menu(menubar,tearoff=0)
editMenu.add_command(label="Undo",command=doNothing)
editMenu.add_command(label="Redo",command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Cut",command=doNothing)
editMenu.add_command(label="Copy",command=doNothing)
editMenu.add_command(label="Paste",command=doNothing)
menubar.add_cascade(label="EDIT",menu=editMenu)

helpMenu = Menu(menubar,tearoff=0)
helpMenu.add_command(label="Help Index",command=doNothing)
helpMenu.add_command(label = "About" , command=doNothing)
menubar.add_cascade(label="HELP",menu=helpMenu)

root.config(menu=menubar)
root.mainloop()







