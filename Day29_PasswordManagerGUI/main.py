import random
from tkinter import *
from tkinter import messagebox
import math
import time
from random import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password = ""
    password_entry.delete(0,END)
    for _ in range(8):
        randvalue = randint(33, 125)
        strrandvalue = chr(randvalue)
        password += strrandvalue
    password_entry.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_entry.get()
    email_id = email_entry.get()
    password_value = password_entry.get()

    if len(website_name) < 1 or len(email_id) < 1 or len(password_value) < 1:
        messagebox.showerror(title="Missing Details", message="Please input all the necessary details...")
    else:
        record = website_name + " | " + email_id + " | " + password_value + "\n"

        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered:\nUsername: {email_id}\nPassword: {password_value}\nIs it okay to save?")

        if is_ok:
            f = open("passwords.txt", "a")
            f.write(record)
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0, "myemailid@myemailserver.de")
password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()