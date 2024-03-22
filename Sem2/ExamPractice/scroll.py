import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Messagebox Example")

def show_message():
    messagebox.showinfo("Info", "Hello, Tkinter!")

button = tk.Button(root, text="Show Message", command=show_message)
button.pack()

root.mainloop()
