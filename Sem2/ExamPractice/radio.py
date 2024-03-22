import tkinter as tk

def show_selected():
    selected_value.set(f"Selected: {selected_option.get()}")

root = tk.Tk()
root.title("Radio Buttons Example")

selected_option = tk.StringVar()
selected_option.set(None)

# Create radio buttons
radio_button1 = tk.Radiobutton(root, text="Option 1", variable=selected_option, value="Option 1", command=show_selected)
radio_button1.pack()

radio_button2 = tk.Radiobutton(root, text="Option 2", variable=selected_option, value="Option 2", command=show_selected)
radio_button2.pack()

radio_button3 = tk.Radiobutton(root, text="Option 3", variable=selected_option, value="Option 3", command=show_selected)
radio_button3.pack()

selected_value = tk.StringVar()
selected_label = tk.Label(root, textvariable=selected_value)
selected_label.pack()

root.mainloop()
