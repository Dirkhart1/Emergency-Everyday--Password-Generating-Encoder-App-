import tkinter as tk
from encode import *

def number_codes():
  password = password_entry.get()
  code = num1_entry.get()
  list = []
  for i in code:
     list.append(i)
  num1 = int(list[0])
  num2 = int(list[1])
  num3 = int(list[2])
  temp = encode(password, num1, num2, num3)
  encoded_password.set(temp)

# This ensures that a the number codes are ONLY numbers
# This program is created with ONLY 3 number digits in mind
# modifing this to allow more wouldn't break the code, but after 3 digits the extra numbers would only hang around
def validate_input(value):
    if len(value) > 3:
      return False
    if value.isdigit() or value == "":
      return True
    else:
       return False

# (WIP - currently unused) This ensures that the encoded password is NOT a entry to type in
# def alwaysFalse(value):
#   return False

# GUI
root = tk.Tk()
root.title("Emeergency Everyday")
root.geometry("600x500+700+250")
root.configure(bg='black')

#Makes window fixed
root.resizable(False, False)

#creates frame
header_frame = tk.Frame(root, bg="black", pady=20)
header_frame.pack(fill=tk.X)

form_frame = tk.Frame(root, padx=20, pady=20, bg="black")
form_frame.pack()

# Add Widgets to header frames
header_label = tk.Label(header_frame, text="Emergency Everyday", font=("Cascadia Code", 24), fg="green", bg="black")
header_label.pack()

# This part adds the input and label for the password
# Adds widgets to form frame
password_label = tk.Label(form_frame, text="Password : ", font=("Cascadia Code", 12), fg="green", bg="black")
password_label.grid(row=0, column=0, sticky=tk.E)
password_entry = tk.Entry(form_frame, font=("Cascadia Code", 12), fg="green", bg="black")
password_entry.grid(row=0, column=1, ipady=3, ipadx=30)


# number codes
num1_code_label = tk.Label(form_frame, text="Encrypter (3 digits) : ", font=("Cascadia Code", 12), fg="green", bg="black")
num1_code_label.grid(row=1, column=0, padx = 3)
num1_entry = tk.Entry(form_frame, validate="key", validatecommand=(root.register(validate_input), '%P'), font=("Cascadia Code", 12), fg="green", bg="black")
num1_entry.grid(row=1, column=1, ipady=3, ipadx=30, sticky=tk.E)


# This adds a button which returns the encoded password
Generate_button = tk.Button(form_frame, text="Encode", command=number_codes, font=("Cascadia Code", 12), fg="green", bg="black")
Generate_button.grid(row=2,column=1, pady=10,)

# This sets up the section where the encoded password will print\
# while you are able to type in it, it will be overwritten when the encode button is pressed
encoded_password = tk.StringVar()

encoded_label = tk.Label(form_frame, text="Encoded Password : ", font=("Cascadia Code", 12), fg="green", bg="black")
encoded_label.grid(row=3, column=0, sticky=tk.E)
encoded_entry = tk.Entry(form_frame, textvariable=encoded_password, font=("Cascadia Code", 12), fg="green", bg="black")
encoded_entry.grid(row=3, column=1, ipady=3, ipadx=30)

advice = """TIP\n
NIST guidance recommends that a password should be at least 15 characters long.

FUN FACT\n
NIST no longer recommends that passwords require special characters and numbers.
Longer Passwords are a higher priority for creating a good password.
But still including those will still help make a more secure password"""

text = tk.Label(text=advice, font=("Cascadia Code", 9), bg="black", fg="green")
text.pack()

root.mainloop()