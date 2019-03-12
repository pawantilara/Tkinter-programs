#counting numbers
import tkinter as tk
counter=0
def counter_label(label):
    def count():
        global counter
        counter+=1
        label.after(1000,count)
    
    tk.Label(root,text="sirf").pack()   
    label.config(text=str(counter))
    
    count()
    
    
    
        
root=tk.Tk()
root.title("Counting Seconds")
label=tk.Label(root,fg="green")
label.pack()
counter_label(label)
button=tk.Button(root,text='Stop',width=25,command=root.destroy)
button.pack()
root.mainloop()

