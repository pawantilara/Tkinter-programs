from tkinter import *

def donothing():
    print("ok okmi won't")
root=Tk()
menu=Menu(root)

root.config(menu=menu)

submenu=Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New Project..",command=donothing)
submenu.add_command(label="New..",command=donothing)
submenu.add_separator()
submenu.add_command(label="Exit",command=donothing)

editMenu=Menu(menu,tearoff=0)
menu.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Redo",command=donothing)

root.mainloop()
