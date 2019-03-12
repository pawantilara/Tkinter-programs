import tkinter as tk
r=tk.Tk()
w=tk.Label(r,text="Hello Tkinter!")
w.pack()
r.mainloop()
#label is a tkinter Widget class which is used to display text or an image
'''
To intitialize tkinter we have to create a tk root widget , which is a window
with title bar and other decoration provided by the window  manager.
The root widget has to be created before any other widgets and there can only be
one root widgets
root=tk.Tk()

//
the next line of code contains the label widget .
the first parameter of the label call is the name of the parent parameter window. in our case root.
so our label widget is a child of the root wodget . the keyword "text" specifies
the text to be shown

//
w.pack()
it tells to fit the size of the window to the given text.

//
root.mainloop()
our script will remain int the event loop until we close the window'''


