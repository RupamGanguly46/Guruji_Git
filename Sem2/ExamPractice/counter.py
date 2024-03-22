import tkinter as tk

root=tk.Tk()
root.geometry("500x500+10+10")
root.minsize(300,300)
root.maxsize(1000,1000)


frame1=tk.Frame(root,relief='solid',bd=2,height=400,width=400)
frame1.pack(side="top")

frame2=tk.Frame(root,relief='solid',bd=2)
frame2.pack(side="bottom")

def inc():
    value=intvar.get()
    intvar.set(value+1)
    labelcount.config(fg="green",font=("helvetica",intvar.get()))


def dec():
    value=intvar.get()
    if value>0:
        intvar.set(value-1)
    labelcount.config(fg="red",font=("helvetica",intvar.get()))

intvar=tk.IntVar(root,1)

buttoninc=tk.Button(frame2,text="Increase",bg="green",fg='white',command=inc)
buttoninc.grid(row=0,column=0)

buttondec=tk.Button(frame2,text="Decrease",bg="red",fg="white",command=dec)
buttondec.grid(row=1,column=0)

labelcount=tk.Label(frame1,textvariable=str(intvar),fg="green",font=("helvetica",intvar.get()))
labelcount.pack()

root.mainloop()

