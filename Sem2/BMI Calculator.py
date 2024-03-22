import tkinter as tk

root=tk.Tk()
root.geometry('500x500')
# root.maxsize(1920,1080)
# root.minsize(1200,720)
root.title("BMI Calculator")
root.resizable()

def calcul():
    height=float(entry1.get())**2
    weight=float(entry2.get())
    bmi=weight/height
    lb3.config(text=bmi)

lb1=tk.Label(root,text="Height in meter")
lb1.grid(row=1,columnspan=3,column=2)

entry1=tk.Entry(root,width=50)
entry1.grid(row=2,columnspan=2,column=1)

lb2=tk.Label(root,text="Weight in kilograms")
lb2.grid(row=3,columnspan=3,column=2)

entry2=tk.Entry(root,width=50)
entry2.grid(row=4,columnspan=3,column=2)

button1=tk.Button(root,text="Submit",command=calcul)
button1.grid(row=5,columnspan=3,column=2)

lb3=tk.Label(root,text="")
lb3.grid(row=6,columnspan=3,column=2)

root.mainloop()


