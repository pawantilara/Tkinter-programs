from tkinter import *
from tkinter import ttk
root = Tk()
text = Text(root)

buttonsFrame = Frame(root)
start = Button(buttonsFrame)
start["text"] = "Start"
start.grid(row = 0, column=1)
stop = Button(buttonsFrame, )
stop["text"] = "Stop"
stop.grid(row = 0, column=3)
buttonsFrame.pack(side=TOP)

tabbedPane = ttk.Notebook(root)

raw =  ttk.Frame(tabbedPane)
interpreted =  ttk.Frame(tabbedPane)
text = Text(raw)
text.pack(fill=BOTH, expand=1, side=TOP)

textInterpreted = Text(interpreted)
textInterpreted.pack(fill=BOTH, expand=1, side=TOP)

tabbedPane.add(raw, text="RAW")
tabbedPane.add(interpreted, text="Application")
tabbedPane.pack(fill=BOTH, expand=1, side=TOP)
checkBoxesFrame = Frame(root)
stkCheck = Checkbutton(checkBoxesFrame, text="STK/CAT")
stkCheck.pack(side=LEFT)
stkFile = Checkbutton(checkBoxesFrame, text="File IO")
stkFile.pack(side=LEFT)
stkAuth = Checkbutton(checkBoxesFrame, text="Auth")
stkAuth.pack(side=LEFT)
checkBoxesFrame.pack()

root.mainloop()
