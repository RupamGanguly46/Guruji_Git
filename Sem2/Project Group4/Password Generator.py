from tkinter import *
import random
import string

root=Tk()
root.geometry("300x300+0+0")
root.maxsize(1200,720)
root.minsize(200,200)
root.title("Password Generator")

def generate():
    # num_of_char=int(passlen.get())
    # while True:
    #     result = ''.join(random.choices(string.punctuation + string.digits + string.ascii_letters, k = num_of_char ))    
        
    #     digcheck=0
    #     lowlettercheck=0
    #     uplettercheck=0
    #     specialcheck=0
        
    #     for low, in string.ascii_lowercase:
    #         if low in result:
    #             lowlettercheckcheck=1
    #             break
    #     for up in string.ascii_uppercase:
    #         if up in result:
    #             uplettercheck=1
    #             break
    #     for digit in string.digits:
    #         if digit in result:
    #             digcheck=1
    #             break
    #     for mark in string.punctuation:
    #         if mark in result:
    #             specialcheck=1
    #             break
        
    #     if digcheck==1 and lowlettercheck==1 and uplettercheck==1 and specialcheck==1:
    #             break
    num_of_char = int(passlen.get())

    while True:  # Loop until a valid password is generated
        result = ''.join(random.choices(
            string.punctuation + string.digits + string.ascii_letters,
            k=num_of_char
        ))

        if all(c in result for c in "!@#$%^&*()_+-=[]{}|;':\",.<>/?~`"):  # Check for special characters efficiently
            break  # Exit the loop if all criteria are met
            
    passbox.config(state="normal")
    passbox.delete(1.0, END)
    passbox.insert(END, result)
    passbox.config(state="disabled")

passbox = Text(root, height=5, width=30, wrap="word", state="disabled")
passbox.grid()

passlen = Spinbox(root, from_ = 8, to =100 )
passlen.grid()

generate_button=Button(root,text="Generate",command=generate)
generate_button.grid()
root.mainloop()




