import tkinter as tk
from tkinter import filedialog
from encode import *


class EmergencyEverydayApp(tk.Tk):

  def __init__(self, *args, **kwargs):

    tk.Tk.__init__(self, *args, **kwargs)

    self.title("Emergency Everyday")
    x = (self.winfo_screenwidth()//2)-(500//2)
    y = (self.winfo_screenheight()//2)-(600//2)
    self.geometry("{}x{}+{}+{}".format(600, 500, x, y))
    self.iconbitmap('EmergencyEverydayIcon.ico')

    #Makes window fixed
    self.resizable(False, False)

    #Containers for the pages
    container = tk.Frame(self)
    container.pack(side = "top" ,fill="both", expand=True)
    
    #Configure grid layout
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    # Dictionary to store page frames
    self.frames = {}

    # Adds pages to the container
    for F in (Main_Page, Help_Page):
      frame = F(container, self)
      self.frames[F] = frame
      frame.grid(row = 0, column = 0, sticky ="nsew")

    self.show_frame(Main_Page) #Shows the Main Menu first

  def show_frame(self, cont):
    # Brings the next frame that gets called
      frame = self.frames[cont]
      frame.tkraise()

class Main_Page(tk.Frame):
  def __init__(self, parent, controller): 
    tk.Frame.__init__(self, parent)
    
    def switch1():
      if password_entry.config("show")[-1] == "*":          
          password_entry.configure(show="")
          show_password_button.config(text="Hide")
      else:
        password_entry.configure(show="*")
        show_password_button.config(text="Show")
    
    def switch2():
      if encrypter_digits.config("show")[-1] == "*":          
          encrypter_digits.configure(show="")
          show_encrpter_digits.config(text="Hide")
      else:
        encrypter_digits.configure(show="*")
        show_encrpter_digits.config(text="Show")

    def switch3():
      if encoded_entry.config("show")[-1] == "*":          
          encoded_entry.configure(show="")
          show_encoded_pass.config(text="Hide")
      else:
        encoded_entry.configure(show="*")
        show_encoded_pass.config(text="Show")
        
        
    def number_codes():
      password = password_entry.get()
      code = encrypter_digits.get()
      list = []
      for i in code:
        list.append(i)
      num1 = int(list[0])
      num2 = int(list[1])
      num3 = int(list[2])
      temp = encode(password, num1, num2, num3)
      encoded_password.set(temp)

    # This allows you to save the password onto a text file
    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            text_content = encoded_password.get()
            with open(file_path, "w") as file:
                file.write(text_content)

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

    # GUI 
    self.configure(bg="black")

    #creates frame
    header_frame = tk.Frame(self, bg="black", pady=25)
    header_frame.pack(fill=tk.X)

    form_frame = tk.Frame(self, padx=20, pady=0, bg="black")
    form_frame.pack()

    # Add Widgets to header frames
    header_label = tk.Label(header_frame, text="Emergency Everyday",
                            font=("Cascadia Code", 24),
                            fg="#149414", bg="black")
    header_label.pack()

    # This part adds the input and label for the password
    # Adds widgets to form frame
    password_label = tk.Label(form_frame, text="Password : ",
                              font=("Cascadia Code", 12),
                              fg="#149414", bg="black")
    password_label.grid(row=0, column=0, pady=20, sticky=tk.E)

    password_entry = tk.Entry(form_frame, show="*",
                              font=("Cascadia Code", 12),
                              fg="#149414", bg="black")
    password_entry.grid(row=0, column=1, ipady=3, ipadx=30)

    show_password_button = tk.Button(form_frame, text="Show",
                                     font=("Cascadia Code", 11),
                                     fg="#149414", bg="black",
                                     command= switch1,
                                     width=5, height=1)
    show_password_button.grid(row=0, column=3, padx=10)

    # number codes
    num1_code_label = tk.Label(form_frame, 
                              text="Encrypter (3 digits) : ",
                              font=("Cascadia Code", 12),
                              fg="#149414", bg="black")
    num1_code_label.grid(row=1, column=0, pady=20)

    encrypter_digits = tk.Entry(form_frame, validate="key", show="*",
                                validatecommand=(self.register(validate_input), '%P'),
                                font=("Cascadia Code", 12),
                                fg="#149414", bg="black")
    encrypter_digits.grid(row=1, column=1, ipady=3, ipadx=30, sticky=tk.E)

    show_encrpter_digits = tk.Button(form_frame, text="Show",
                                     font=("Cascadia Code", 11),
                                     fg="#149414", bg="black",
                                     command= switch2,
                                     width=5, height=1)
    show_encrpter_digits.grid(row=1, column=3, padx=10)

    # This adds a button which returns the encoded password
    Generate_button = tk.Button(form_frame, text="Encode", command=number_codes,
                                font=("Cascadia Code", 12), fg="#149414", bg="black",
                                activebackground="#149414", activeforeground="black")
    Generate_button.grid(row=2,column=1, pady=20,)

    # This sets up the section where the encoded password will print\
    # while you are able to type in it, it will be overwritten when the encode button is pressed
    encoded_password = tk.StringVar()

    encoded_label = tk.Label(form_frame,
                            text="Encoded Password : ",
                            font=("Cascadia Code", 12),
                            fg="#149414", bg="black")
    encoded_label.grid(row=3, column=0, pady=20, sticky=tk.E)

    encoded_entry = tk.Entry(form_frame, show="*",
                            textvariable=encoded_password,
                            font=("Cascadia Code", 12),
                            fg="#149414", bg="black")
    encoded_entry.grid(row=3, column=1, ipady=3, pady=20, ipadx=30)

    show_encoded_pass = tk.Button(form_frame, text="Show",
                                  font=("Cascadia Code", 11),
                                  fg="#149414", bg="black",
                                  command= switch3,
                                  width=5, height=1)
    show_encoded_pass.grid(row=3, column=3, padx=10)

    # This creates a SAVE button to store your password into a text file
    Help_Button = tk.Button(form_frame, text="Help",
                            font=("Cascadia Code", 12),
                            fg="#149414", bg="black",
                            activebackground="#149414",
                            activeforeground="black",
                            command = lambda : controller.show_frame(Help_Page))
    Help_Button.grid(row=4, column=0, pady=20)
    Save_Button = tk.Button(form_frame, text="Save", 
                            command=save_file,
                            font=("Cascadia Code", 12),
                            fg="#149414", bg="black",
                            activebackground="#149414",
                            activeforeground="black")
    Save_Button.grid(row=4,column=1, pady=20)

class Help_Page(tk.Frame):
  def __init__(self, parent, controller):        
    tk.Frame.__init__(self, parent)
    self.configure(bg="black")

    advice =("Emergency Everyday is a program designed to help Users create a\n" +
             "strong password using simple inputs\n\n" +
             "This app only requires you to fill out two entries :\n" \
             "A password (can be as simple as password123)\n" \
             "A three (3) digit code\n\n" +
             "Then you press the \"encode\" button and you'll get\n" \
             "an encrypted version of your code\n\n"
             "- - - - TIP - - - -\n\n" \
            "NIST guidance recommends that a password should\n" +
            "be at least 8 characters long.\n\n" \
            "- - - - FUN FACT - - - -\n\n" \
            "NIST no longer recommends that passwords require\n" +
             "special characters and numbers.\n\n" \
            "Longer Passwords are a higher priority for creating a good password.\n" \
            "But including those will still help make a more secure password"
            )
    text = tk.Label(self, text=advice, anchor="center",font=("Cascadia Code", 10), bg="black", fg="#149414")
    text.grid(row=1,pady=20, padx=20, )
 
    # This will allow navigation back to the main page
    button1 = tk.Button(self, text ="Back",
                        font=("Cascadia Code", 12),
                        fg="#149414", bg="black",
                        activebackground="#149414",
                        activeforeground="black",
                        command = lambda : controller.show_frame(Main_Page))
    button1.grid(row = 7, column = 0, sticky=tk.NS)

app = EmergencyEverydayApp()
app.mainloop()