from tkinter import *
root=Tk()
root.title("Prime Number Checker")
root.geometry('800x600+200+80')
root.maxsize(1000,1000)
root.minsize(500,500)
labtxt=StringVar(root,"")
boxtxt=IntVar(root,0)

def pattern():
    rows=boxtxt.get()
    txt=''
    for row in range(1,rows+1):
        for cell in range(row):
            txt+="*"
        txt+='\n'
    labtxt.set(txt)

lab1=Label(root,text="Enter number of rows for pattern :")
lab1.pack()

box=Entry(root,text=boxtxt)
box.pack()

but=Button(root,text="Enter",command=pattern)
but.pack()

lab2=Label(root,textvariable=labtxt,justify="left")
lab2.pack()

root.mainloop()

