from tkinter import *
root=Tk()
root.title('')
root.geometry('500x500')
root.maxsize(600,600)
root.minsize(100,100)
lbtxt=StringVar(root,"")
buttxt=StringVar(root,"")
root.resizable(False,False)
buttonpressed=0

def butfunc():
    global buttonpressed
    if buttonpressed==0:
        buttxt.set('')
        lbtxt.set('')
    else:
        buttxt.set(' ')
        data=lbtxt.get()+' '
        lbtxt.set(data)
    buttonpressed=1
    


lb=Label(root,textvariable=lbtxt)
lb.pack()

but=Button(root,textvariable=buttxt,command=butfunc)
but.pack()

root.mainloop()


