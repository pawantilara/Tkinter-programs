from tkinter import *

class pawanButton:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()

        self.printButton=Button(frame,text="do whatever you want",command=self.printmessage).pack(side=LEFT)
        self.quitbutton=Button(frame,text="Quit",command=frame.quit).pack(side=LEFT)
    def printmessage(self):
        print("you are doing good")

        





root=Tk()
b=pawanButton(root)
root.mainloop()
