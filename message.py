from tkinter import *
import tkinter.messagebox

var = Tk()
tkinter.messagebox.showinfo('code in python', 'this is the tkinter tutorial')
ans = tkinter.messagebox.askquestion('quiz', 'do you like python')
if ans == 'yes':
   print("welcome to codeinpython.com")
else:
    command=var.quit

var.mainloop() 
