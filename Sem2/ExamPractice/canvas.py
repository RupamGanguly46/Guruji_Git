import tkinter as tk

def focus_in(event):
    canvas.config(bg="lightblue")
    canvas2.config(bg="white")

def focus_out(event):
    canvas.config(bg="white")
    canvas2.config(bg="lightblue")
    

root = tk.Tk()
root.title("Canvas Highlight Color Example")

canvas = tk.Canvas(root, width=400, height=400, bg="white", highlightcolor="red")
canvas.pack()

# Bind events to change canvas background color
canvas.bind("<FocusIn>", focus_in)
canvas.bind("<FocusOut>", focus_out)

canvas2 = tk.Canvas(root, width=400, height=400, bg="white", highlightcolor="blue")
canvas2.pack()

# Bind events to change canvas background color
canvas2.bind("<FocusIn>", focus_in)
canvas2.bind("<FocusOut>", focus_out)

root.mainloop()