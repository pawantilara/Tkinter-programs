from tkinter import *
root=Tk()
top=Frame(root)
top.pack()
bottom=Frame(root)
bottom.pack(side=BOTTOM)

button1=Button(top,text="Button1",fg="red")
button2=Button(top,text="Button2",fg="green")
button3=Button(top,text="Button3",fg="blue")
button4=Button(bottom,text="Button4",fg="purple")
button5=Button(bottom,text="Button5",fg="orange")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)
button5.pack(side=RIGHT)

root.mainloop()


               
