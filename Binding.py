from tkinter import *

root=Tk()

def printname(event):
    print("hello boy")
def printname1(event):
    print("hello hero")
def printname2(event):
    print("hello bob")
#lab=Button(root,text="you are a",command=printname) # first method
lab=Button(root,text="you are a") # second method
lab.bind("<Button-1>",printname)
lab.pack()
frame=Frame(root,width=300,height=250)
frame.bind("<Button-1>",printname)
frame.bind("<Button-2>",printname1)
frame.bind("<Button-3>",printname2)
frame.pack()
root.mainloop
