import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Calculator")
        self.geometry("200x200")
        self.result = tk.Entry(self)
        self.result.grid(row=0, column=0, columnspan=4)
        self.create_button("1", 1, 1)
        self.create_button("2", 1, 2)
        self.create_button("3", 1, 3)
        self.create_button("4", 2, 1)
        self.create_button("5", 2, 2)
        self.create_button("6", 2, 3)
        self.create_button("7", 3, 1)
        self.create_button("8", 3, 2)
        self.create_button("9", 3, 3)
        self.create_button("0", 4, 2)
        self.create_button("+", 5, 1)
        self.create_button("-", 5, 2)
        self.create_button("*", 5, 3)
        self.create_button("/", 6, 1)
        self.create_button(".", 6, 2)
        self.create_button("=", 6, 3, lambda: self.calculate())
        self.create_button("C", 4, 1, lambda: self.clear())

    def create_button(self, text, row, column, command=lambda: self.add_number(text)):
        button = tk.Button(self, text=text, command=command)
        button.grid(row=row, column=column)

    def add_number(self, number):
        current = self.result.get()
        current += number
        self.result.delete(0, tk.END)
        self.result.insert(0, current)

    def clear(self):
        self.result.delete(0, tk.END)

    def calculate(self):
        current = self.result.get()
        self.result.delete(0, tk.END)