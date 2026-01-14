#https://github.com/TkinterEP/ttkthemes/tree/master/screenshots

from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk

create = ThemedTk(theme = "breeze")
create.geometry("500x250")
create.title("User Sign Up")
create.resizable(False, False)

user_img = PhotoImage(file = "user.png")

create.iconphoto(True, user_img)

login_tries = 0
name = None
password = None
email = None

admin = False

def open_login_window():
    global name, password, email, login_tries, admin

    create.withdraw()
    login = Toplevel(create)
    login.geometry("500x250")
    login.iconphoto(True, user_img)
    login.resizable(False, False)
    if admin:
        login.title("Admin Login")
    else:
        login.title("User Login")

    login.protocol("WM_DELETE_WINDOW", lambda: (login.destroy(), create.destroy()))

    if admin:
        titlelbl2 = Label(login, text="Welcome! Please log in as admin:", background="light blue", font=("Rubik Mono One", 13))
    else:
        titlelbl2 = Label(login, text="Welcome back! Please log in:", background="light blue", font=("Rubik Mono One", 15))
    titlelbl2.pack()

    lbl4 = Label(login, text="Username:", background="#B8F4FF", font=("Rubik Mono One", 12))
    lbl4.place(x=0, y=50)

    lbl5 = Label(login, text="Password:", background="#B8F4FF", font=("Rubik Mono One", 12))
    lbl5.place(x=0, y=90)

    lbl6 = Label(login, text="Email:", background="#B8F4FF", font=("Rubik Mono One", 12))
    lbl6.place(x=0, y=130)

    txt4 = Entry(login, background="#DADBDD")
    txt4.place(x=170, y=45)

    txt5 = Entry(login, background="#DADBDD", show="•")
    txt5.place(x=170, y=85)

    txt6 = Entry(login, background="#DADBDD")
    txt6.place(x=170, y=125)

    def check_login():
        entry_name2 = txt4.get().strip()
        entry_password2 = txt5.get().strip()
        entry_email2 = txt6.get().strip()

        if not entry_name2 or not entry_password2 or not entry_email2:
            titlelbl.configure(text="Please fill all of the fields", foreground="red")
            return

        if admin:
            if entry_name2 == "AlexIsNotInset" and entry_password2 == "12345678" and entry_email2 == "inset@python.com":
                titlelbl2.configure(text="Logged in as Admin.", foreground="blue")
                login.title("Admin Login Successful")
            else:
                titlelbl2.configure(text="Incorrect credentials.", foreground="red")
                login.title("Login Failed")
        else:
            if entry_name2 == name and entry_password2 == password and entry_email2 == email:
                titlelbl2.configure(text="Logged in as User.", foreground="green")
                login.title("User Login Successful")
            else:
                titlelbl2.configure(text="Incorrect credentials.", foreground="red")
                login.title("Login Failed")

    button_style3 = Style()
    button_style3.configure("login.TButton", font=("Rubik Mono One", 12))

    Button(login, text="Log In", style = "login.TButton", width=10, command = check_login).place(x = 170, y = 200)

def create_account():
    global name, password, email, login_tries

    entry_name = txt.get().strip()
    entry_password = txt2.get().strip()
    entry_email = txt3.get().strip()

    if not entry_name or not entry_password or not entry_email or (entry_name == "AlexIsNotInset" and entry_password == "12345678" and entry_email == "inset.alex@gmail.com"):
        login_tries += 1
        msg = f"Please fill all of the fields (x{login_tries})" if login_tries > 1 else "Please fill all of the fields"
        titlelbl.configure(text=msg, foreground="red", background="#FF8C8C", font = ("Rubik Mono One", 12))
        create.title("Sign Up Failed")
        return

    symbols = "!@#$%^&*()-_+=<>?/.,:;"

    has_upper = False
    has_number = False
    has_symbol = False

    for char in entry_password:
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_number = True
        if char in symbols:
            has_symbol = True

    if len(entry_password) >= 6 and has_upper and has_number and has_symbol:
        pass
    else:
        create.title("Sign Up Failed")
        titlelbl.configure(text="Invalid Password", foreground="red")
        return

    if "@" in entry_email:
        pass
    else:
        create.title("Sign Up Failed")
        titlelbl.configure(text="Invalid Email", foreground="red")
        return

    name, password, email = entry_name, entry_password, entry_email
    titlelbl.configure(text="Account Created.", foreground="green")
    create.title("Creation Successful")
    btn.config(state=DISABLED)

    titlelbl.after(1500, open_login_window)

def admin_login():
    global admin

    admin = True
    open_login_window()

titlelbl = Label(create, text="Create account to continue:", background="light blue", font=("Rubik Mono One", 15))
titlelbl.pack()

Label(create, text="Enter your username:", background="#B8F4FF", font=("Arial", 12)).place(x=0, y=50)
Label(create, text="Enter your password:", background="#B8F4FF", font=("Arial", 12)).place(x=0, y=90)
Label(create, text="Enter your email:", background="#B8F4FF", font=("Arial", 12)).place(x=0, y=130)

Label(create, text="Password needs: A capital letter, A number, A symbol, at least 6 characters", foreground = "gray", background="#DADBDD", font=("Arial", 10)).place(x=0, y=200)

txt = Entry(create, background="#DADBDD")
txt.place(x=160, y=45)

txt2 = Entry(create, background="#DADBDD", show="•")
txt2.place(x=160, y=85)

txt3 = Entry(create, background="#DADBDD")
txt3.place(x=160, y=125)

button_style = Style()
button_style.configure("TButton", font = ("Rubik Mono One", 10))

btn = Button(create, text="Sign Up", style = "TButton", width=10, command=create_account)
btn.place(x=350, y=60)

button_style2 = Style()
button_style2.configure("Admin.TButton", font = ("Rubik Mono One", 7))

btn2 = Button(create, text="I'm an admin.", style = "Admin.TButton", command=admin_login)
btn2.place(x=354, y=90)

create.mainloop()
