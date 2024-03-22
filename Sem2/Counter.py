# do not name your file as tkinter.py as it causes error
# Python modules are imported based on filenames. So, when you tried to import Tkinter using import tkinter, Python attempted to import your file instead of the built-in Tkinter module. Since your file didn't define a Tk class, you received an AttributeError.

from tkinter import *

class Counter:
    def __init__(self,mainwindow):
        self.mainwindow=mainwindow
        mainwindow.title("MY APP")
        mainwindow.geometry=("1920x1080")
        mainwindow.maxsize=(1920,1080)
        mainwindow.minsize=(1920,1080)

        # Global initialization
        self.var=IntVar(value=0)
        
        self.lb = Label(mainwindow,textvariable=self.var,font=("bold",30),fg='green')
        self.lb.pack()
        self.bt1=Button(mainwindow,text="Increment",command=self.increment)
        self.bt1.pack(side=LEFT,ipadx=10,ipady=10,padx=10,pady=10)
        self.bt2=Button(mainwindow,text="Decrement",command=self.decrement)
        self.bt2.pack(side=RIGHT,ipadx=10,ipady=10,padx=10,pady=10)

        mainwindow.mainloop()
    def increment(self):
        data = self.var.get() + 1
        self.var.set(data)
        if data>=10:
            self.lb.config(fg='red')
        else:
            self.lb.config(fg='green')

    def decrement(self):
        data = self.var.get() - 1
        if data>=0:
            self.var.set(data)
        if data>=10:
            self.lb.config(fg='red')
        else:
            self.lb.config(fg='green')



# main window
root = Tk()
exe=Counter(root)




# root.counter=0






