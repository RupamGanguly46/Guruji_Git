import tkinter as tk

def hide_label():
    label.pack_forget()

def show_label():
    label.pack(before=hide_button)

root = tk.Tk()

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

hide_button = tk.Button(root, text="Hide Label", command=hide_label)
hide_button.pack()

show_button = tk.Button(root, text="Show Label", command=show_label)
show_button.pack()

root.mainloop()
