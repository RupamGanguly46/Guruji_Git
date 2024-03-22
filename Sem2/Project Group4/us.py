import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, complexity, exclude_symbols):
    if complexity == "Low":
        characters = string.ascii_letters + string.digits
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "High":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase
    else:
        raise ValueError("Invalid complexity level. Choose from 'Low', 'Medium', or 'High'.")

    # Remove excluded symbols
    characters = ''.join([c for c in characters if c not in exclude_symbols])

    password = ''.join(random.choice(characters) for _ in range(length))


    return password

def generate():
    try:
        length = int(length_entry.get())
        complexity = complexity_var.get()
        exclude_symbols = exclude_symbols_entry.get()


        unlimited_loop_preventer=0
        error=0
        while True:
            unlimited_loop_preventer+=1

            password = generate_password(length, complexity, exclude_symbols)

            if (any(c.islower() for c in password) and
                    any(c.isupper() for c in password) and
                    any(c.isdigit() for c in password) and
                    any(c in string.punctuation for c in password)):
                break
            
            if unlimited_loop_preventer>100:
                error=1
                break

        if error==1:
            # You need to press generate again and show error

        result_label.config(text="Generated password: " + password)

        if error==1:
            messagebox.showerror("Error", e)

        
    except ValueError as e:
        messagebox.showerror("Error", e)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Length label and entry
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)

# Complexity label and dropdown
complexity_label = tk.Label(root, text="Complexity Level:")
complexity_label.grid(row=1, column=0, padx=5, pady=5)
complexity_var = tk.StringVar(root)
complexity_dropdown = tk.OptionMenu(root, complexity_var, "Low", "Medium", "High")
complexity_dropdown.grid(row=1, column=1, padx=5, pady=5)
complexity_var.set("Medium")  # Default value

# Exclude symbols label and entry
exclude_symbols_label = tk.Label(root, text="Exclude Symbols:")
exclude_symbols_label.grid(row=2, column=0, padx=5, pady=5)
exclude_symbols_entry = tk.Entry(root)
exclude_symbols_entry.grid(row=2, column=1, padx=5, pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate)
generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
