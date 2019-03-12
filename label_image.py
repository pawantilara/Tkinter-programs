import tkinter as tk
root=tk.Tk()
'''#logo=tk.PhotoImage(file="th.gif")
#w1=tk.Label(root,image=logo).pack(side="right")
explanantion="its really good to see taht i moved forward i am working great"
w2=tk.Label(root,justify=tk.LEFT,padx=10,text=explanantion).pack(side="left")
root.mainloop()'''
tk.Label(root,text="Red Text in times front",fg="red",font="Times").pack()
tk.Label(root,text="Green Text in helventica font",fg="light green",bg="dark green",font="Helvetica 16 bold italic").pack()
root.mainloop()
