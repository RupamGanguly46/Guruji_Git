import tkinter as tk

root = tk.Tk()
root.title("Frames Example")

# Create a frame
frame1 = tk.Frame(root, borderwidth=2, relief="ridge")
frame1.pack(side="left", padx=10, pady=10)

# Add widgets to the frame
label1 = tk.Label(frame1, text="This is Frame 1")
label1.grid(row=1,column=1)

button1 = tk.Button(frame1, text="Click Me")
button1.grid(row=1,column=2)

# Create another frame
frame2 = tk.Frame(root, borderwidth=2, relief="ridge")
frame2.pack(side="right", padx=10, pady=10)

# Add widgets to the second frame
label2 = tk.Label(frame2, text="This is Frame 2")
label2.pack()

button2 = tk.Button(frame2, text="Click Me")
button2.pack()



# Add widgets to the third frame
frame3 = tk.Frame(root, width=200, height=200, borderwidth=2, relief="ridge")
frame3.pack(side="bottom", padx=10, pady=10)

# Add widgets to the third frame
label3 = tk.Label(frame3, text="This is Frame 3")
label3.place(x=100,y=50)

button3 = tk.Button(frame3, text="Click Me")
button3.place(x=100,y=100)

root.mainloop()
