from tkinter import *

root=Tk()
Label(root,text="Description").grid(row=0,column=0,sticky=W)
Entry(root,width=50).grid(row=0,column=1)
Button(root,text="Submit").grid(row=0,column=8)

Label(root,text="Quality").grid(row=1,column=0,sticky=W)
Radiobutton(root,text="New",value=1).grid(row=2,column=0,sticky=W)
Radiobutton(root,text="Good",value=2).grid(row=3,column=0,sticky=W)

Radiobutton(root,text="Poor",value=3).grid(row=4,column=0,sticky=W)

Radiobutton(root,text="Damaged",value=4).grid(row=5,column=0,sticky=W)

Label(root,text="Benifits").grid(row=1,column=1,sticky=W)
Checkbutton(root,text="Free Shipping").grid(row=2,column=1,sticky=W)
Checkbutton(root,text="Bonus Gifts").grid(row=3,column=1,sticky=W)
Label(root,text="a ").grid(row=6,column=0,sticky=S)



def get_sum(event):
    num1=int(num1Entry.get())
    num2=int(num2Entry.get())
    sumEntry.delete(0,"end")
    sum=num1+num2
    sumEntry.insert(0,sum)

num1Entry=Entry(root)
num1Entry.pack(side=LEFT)

Label(root,text="+").pack(side=LEFT)

num2Entry=Entry(root)
num2Entry.pack(side=LEFT)

equalButton=Button(root,text="=")
equalButton.bind("<Button-1>",get_sum)
equalButton.pack(side=LEFT)

sumEntry=Entry(root)
sumEntry.pack(side=LEFT)  





root.mainloop()
