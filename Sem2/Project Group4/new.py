# this code generates password many times in order to fetch a single valid password

from tkinter import *
import random
import string

root = Tk()
root.geometry("300x300+0+0")
root.maxsize(1200, 720)
root.minsize(200, 200)
root.title("Password Generator")

def generate():
    num_of_char = int(passlen.get())

    while True:
        result = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=num_of_char))

        # Checks for each condition
        if (any(c.islower() for c in result) and
                any(c.isupper() for c in result) and
                any(c.isdigit() for c in result) and
                any(c in string.punctuation for c in result)):
            break  # If all conditions are met, exit the loop

    passbox.config(state="normal")
    passbox.delete(1.0, END)
    passbox.insert(END, result)
    passbox.config(state="disabled")

passbox = Text(root, height=5, width=30, wrap="word", state="disabled")
passbox.grid()

passlen = Spinbox(root, from_=8, to=100)
passlen.grid()

generate_button = Button(root, text="Generate", command=generate)
generate_button.grid()

root.mainloop()