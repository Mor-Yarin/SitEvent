from tkinter import *
from tkinter.ttk import  *

root=Tk()
root.iconbitmap('icon.ico')
root.title("SitEvent")
s=Style()
s.configure('but.TButton', font=('David', 12))
s.configure('titleS.TLabel', font=('Felix Titling', 12))


title1=Label(root, text="Sit Event",style='titleS.TLabel')
title1.pack()

newUser=Button(root,text="New user",style='but.TButton')
newUser.pack()

exUser=Button(root,text="Existing user",style='but.TButton')
exUser.pack()


root.mainloop()