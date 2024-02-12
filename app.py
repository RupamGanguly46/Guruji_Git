from tkinter import *
root=Tk()
root.title('Naughty App')
root.geometry('500x500')
root.maxsize(600,600)
root.minsize(100,100)
lbtxt=StringVar(root,"Heyyy Boy!")
buttxt=StringVar(root,"Push me Baby!")
root.resizable(False,False)
buttonpressed=0

def butfunc():
    global buttonpressed
    if buttonpressed==0:
        buttxt.set('Push me harder! ')
        lbtxt.set('Aah!')
    else:
        buttxt.set('Harder!! ')
        data=lbtxt.get()+' AAH!'
        lbtxt.set(data)
    buttonpressed=1
    


lb=Label(root,textvariable=lbtxt)
lb.pack()

but=Button(root,textvariable=buttxt,command=butfunc)
but.pack()

root.mainloop()


