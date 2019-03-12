from tkinter import *
def printsomething():
   print("CIP is best for learning python :-P")
var = Tk()
main_menu = Menu(var)
var.config(menu = main_menu)
sub_menu = Menu(main_menu)
main_menu.add_cascade(label = "File")
sub_menu.add_command(label = "blank page", command = printsomething)
sub_menu.add_separator()
sub_menu.add_command(label = "open", command = printsomething)
var.mainloop() 
