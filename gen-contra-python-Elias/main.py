from tkinter import *
from tkinter import ttk, simpledialog, messagebox
from ttkbootstrap import Style
import random, string, pyperclip, shutil, datetime, os

class App:
    def __init__(self):

        self.style = Style(theme = "cosmo")
        self.root = self.style.master
        self.root.geometry("700x420")
        self.root.resizable(0, 0)
        self.root.title("CRUFTY password generato o generador de contraseñas")
        self.icon = PhotoImage(file = "res/lock.png")
        self.root.iconphoto(False, self.icon)

        menubar = Menu(self.root)
        self.root.config(menu = menubar)

        filemenu = Menu(menubar)
        filemenu.add_command(label = "Guardar la contraseña", command = self.savepwd)
        menubar.add_cascade(label="Archivo", menu = filemenu)

        managemenu = Menu(menubar)
        managemenu.add_command(label = "Exportar las contraseñas", command = self.exportpwd)
        menubar.add_cascade(label="Administrar", menu = managemenu)
        logo = PhotoImage(file = "res/logo.png")
        Label(self.root, image = logo).pack(pady = 5)
        self.pass_str = StringVar()

        self.genpassword()
        ttk.Entry(self.root, textvariable = self.pass_str, width = 27, justify = CENTER).pack(pady = 5)
        ttk.Button(self.root, text = "GENERAR CONTRASEÑA", command = self.genpassword, width = 25, style='success.TButton').pack(pady = 5)
        ttk.Button(self.root, text = 'COPIAR', command = self.copyPassword, width = 25, style='secondary.TButton').pack(pady = 5)
  
        self.root.mainloop()

    def genpassword(self):
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbol = string.punctuation

        all = lower + upper + num + symbol

        temp = random.sample(all, 16)

        password = "".join(temp)
  
        self.pass_str.set(password)

    def savepwd(self):

        pwd = self.pass_str.get()
        pwd_desc = simpledialog.askstring(title = "Pwd Gen", prompt="Enter your Password Description:", )
        if pwd_desc is not None and len(pwd_desc) > 0:
            with open ("pwd", "a") as file:
                file.write(f"{pwd_desc} {pwd}\n")
                messagebox.showinfo(message=f"Success!\nWe have saved:\nPassword {pwd}\nDescription {pwd_desc}", title="Pwd Gen")
    
    def exportpwd(self):
        now = datetime.datetime.now()
        dt_string = now.strftime("%d%m%Y%H%M%S")
        dir_location = os.getcwd()
        shutil.copyfile("pwd", f"{dt_string}_backup.txt")
        messagebox.showinfo(message = f"Success, find your backup on:\n{dir_location}/{dt_string}_backup.txt", title="Pwd Gen")

    def copyPassword(self):
        pyperclip.copy(self.pass_str.get())

MyApp = App()