from tkinter import *
root=Tk()
root.title("Prime Number Checker")
root.geometry('800x600+200+80')
root.maxsize(1000,1000)
root.minsize(500,500)
labtxt=StringVar(root,"Enter the number :")
boxtxt=IntVar(root,0)

def prime():
    num=boxtxt.get()
    flag=0
    for iter in range(2,num//2):
        if num%iter==0:
            flag=1
            break

    if flag==0:
        labtxt.set(f"{num} is prime. Enter another number :")
    else:
        labtxt.set(f"{num} is composite. Enter another number :")

lab=Label(root,textvariable=labtxt)
lab.pack()

box=Entry(root,text=boxtxt)
box.pack()

but=Button(root,text="Enter",command=prime)
but.pack()

root.mainloop()

