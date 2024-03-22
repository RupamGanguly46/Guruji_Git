from tkinter import *
import random
import string

root=Tk()

def password_generator():

def random_string_generator(anylist):
    if (any([char.isupper() for char in password]) and any([char.islower() for char in password])
    and any([char.isdigit() for char in password]) and any([(char in string.punctuation) for char in password])):
        