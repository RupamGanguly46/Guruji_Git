
import tkinter as tk

root = tk.Tk()
root.title("Listbox Example")

listbox = tk.Listbox(root)
listbox.pack()

# Insert items into the listbox
listbox.insert(tk.END, "Item 1")
listbox.insert(tk.END, "Item 2")
listbox.insert(tk.END, "Item 3")

# Insert items at specific positions
listbox.insert(1, "Inserted Item")

root.mainloop()