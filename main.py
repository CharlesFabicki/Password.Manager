from tkinter import *
from tkinter import messagebox
import pyperclip
import random

# Constants
MIN_PASSWORD_LENGTH = 6
MAX_PASSWORD_LENGTH = 12


# Password Generator
def password_generator():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    password_length = random.randint(MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH)
    password_chars = (
            [random.choice(letters) for _ in range(password_length - 3)]
            + [random.choice(symbols) for _ in range(3)]
            + [random.choice(numbers) for _ in range(3)]
    )

    random.shuffle(password_chars)
    password = ''.join(password_chars)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# Save Password
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not password:
        messagebox.showinfo(title='Error', message='Please input data in the required fields.')
    else:
        confirmation_message = f'New data entered:\nWebsite: {website}\nEmail/Username: {email}\nPassword: {password}\n'
        messagebox.askokcancel(title='Confirmation', message=confirmation_message)

        with open('data.txt', 'a') as data_file:
            data_file.write(f'{website} | {email} | {password}\n')
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# Clear Data
def delete_all():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)


# Exit
def on_exit():
    if messagebox.askyesno("Exit", "Are you sure you want to close the app?"):
        window.destroy()


# ---------------------------- GUI PROGRAM ------------------------------- #

window = Tk()
window.title('Password Manager/Generator')
window.config(padx=50, pady=30, bg='#8B008B')

canvas = Canvas(height=200, width=500, bg='#8B008B')
logo_img = PhotoImage(file='logo.png')
canvas.create_image(275, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text='WEBSITE : ', bg='#8B008B', fg='white', font=('Helvetica', 14, 'bold'))
website_label.grid(row=1, column=0)
email_label = Label(text='E-MAIL/USERNAME : ', bg='#8B008B', fg='white', font=('Helvetica', 14, 'bold'))
email_label.grid(row=2, column=0)
password_label = Label(text='PASSWORD: ', bg='#8B008B', fg='white', font=('Helvetica', 14, 'bold'))
password_label.grid(row=3, column=0)

website_entry = Entry(width=50, bg='white', font=('Helvetica', 14))
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=50, bg='white', font=('Helvetica', 14))
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "")

password_entry = Entry(width=50, bg='white', font=('Helvetica', 14))
password_entry.grid(row=3, column=1, columnspan=2)

generate_password_button = Button(text='Generate Password', width=40, height=2, bg='#4CAF50', fg='white',
                                  font=('Helvetica', 12, 'bold'), command=password_generator)
generate_password_button.grid(row=4, column=1, columnspan=2)

add_button = Button(text='Add a New Password to data.txt', width=40, height=2, bg='#4CAF50', fg='white',
                    font=('Helvetica', 12, 'bold'), command=save)
add_button.grid(row=5, column=1, columnspan=2)

clear_button = Button(text='Clear All Data', width=40, height=2, bg='red', fg='white',
                      font=('Helvetica', 12, 'bold'), command=delete_all)
clear_button.grid(row=6, column=1, columnspan=2)

exit_button = Button(text='Exit', width=40, height=2, bg='black', fg='white', font=('Helvetica', 12, 'bold'),
                     command=on_exit)
exit_button.grid(row=7, column=1, columnspan=2)

window.mainloop()
