from tkinter import *

root=Tk()

label_1=Label(root,text="Name")
label_2=Label(root,text="Password")
enter_1=Entry(root)
enter_2=Entry(root)

label_1.grid(row=0,sticky=E) #sticky is used to align the text in E-east,N=north and so on
label_2.grid(row=1,sticky=E)

enter_1.grid(row=0,column=1)
enter_2.grid(row=1,column=1)

c=Checkbutton(root,text="Keep me loged in")
c.grid(columnspan=2)

root.mainloop()
