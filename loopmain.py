from tkinter import *
root=Tk()
one=Label(root,text="One",fg="red",bg="orange")
one.pack()
two=Label(root,text="two",fg="green",bg="light green")
two.pack(fill=X)
three=Label(root,text="three",fg="purple",bg="blue")
three.pack(side=LEFT,fill=Y)

root.mainloop()
