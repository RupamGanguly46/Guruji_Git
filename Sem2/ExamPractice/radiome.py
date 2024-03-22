from tkinter import *
root=Tk()

def fun():
    labelavar.set(f"{selected.get()} is selected")

selected=StringVar()
selected.set(None)

labelavar=StringVar()

radio1=Radiobutton(root,variable=selected,text='Pehla button',value="1",command=fun)
radio1.pack()

radio2=Radiobutton(root,variable=selected,text='Dusra button',value="2",command=fun)
radio2.pack()

labela=Label(root,textvariable=labelavar)
labela.pack()

root.mainloop()