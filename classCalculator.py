from tkinter import *

class Calculator:
    def __init__(self, name = "Simple Calculator"):
        self.window = Tk()
        self.window.title(name)
        self.window.iconbitmap("calculatorIcon.ico")
        
        self.e = Entry(self.window, width=35, borderwidth = 5)
        self.e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)
        self.e.insert(0, "")

        self.fnum = 0
        self.math = ""

        #number button
        self.button_1 = Button(self.window, text="1", padx = 40, pady = 20, command = lambda: self.button_click(1))
        self.button_2 = Button(self.window, text="2", padx = 40, pady = 20, command = lambda: self.button_click(2))
        self.button_3 = Button(self.window, text="3", padx = 40, pady = 20, command = lambda: self.button_click(3))
        self.button_4 = Button(self.window, text="4", padx = 40, pady = 20, command = lambda: self.button_click(4))
        self.button_5 = Button(self.window, text="5", padx = 40, pady = 20, command = lambda: self.button_click(5))
        self.button_6 = Button(self.window, text="6", padx = 40, pady = 20, command = lambda: self.button_click(6))
        self.button_7 = Button(self.window, text="7", padx = 40, pady = 20, command = lambda: self.button_click(7))
        self.button_8 = Button(self.window, text="8", padx = 40, pady = 20, command = lambda: self.button_click(8))
        self.button_9 = Button(self.window, text="9", padx = 40, pady = 20, command = lambda: self.button_click(9))
        self.button_0 = Button(self.window, text="0", padx = 40, pady = 20, command = lambda: self.button_click(0))
        #operation button
        self.button_add = Button(self.window, text="+", padx = 39, pady = 20, command = self.button_add)
        self.button_equal = Button(self.window, text="=", padx = 91, pady = 20, command = self.button_equal)
        self.button_clear = Button(self.window, text="clear", padx = 79, pady = 20, command = self.button_clear)
        self.button_subtract = Button(self.window, text="-", padx = 41, pady = 20, command = self.button_subtract)
        self.button_multiply = Button(self.window, text="x", padx = 40, pady = 20, command = self.button_multiply)
        self.button_divide = Button(self.window, text="/", padx = 41, pady = 20, command = self.button_divide)

        #location number
        self.place(self.button_1,3,0,1)
        self.place(self.button_2,3,1,1)
        self.place(self.button_3,3,2,1)
        self.place(self.button_4,2,0,1)
        self.place(self.button_5,2,1,1)
        self.place(self.button_6,2,2,1)
        self.place(self.button_7,1,0,1)
        self.place(self.button_8,1,1,1)
        self.place(self.button_9,1,2,1)
        self.place(self.button_0,4,0,1)
        #location operation
        self.place(self.button_add,5,0,1)
        self.place(self.button_clear,4,1,2)
        self.place(self.button_equal,5,1,2)
        self.place(self.button_subtract,6,0,1)
        self.place(self.button_multiply,6,1,1)
        self.place(self.button_divide,6,2,1)

    def button_add(self):
        first_number = self.e.get()
        self.math = "addition"
        self.fnum = int(first_number)
        self.e.delete(0,END)
        return

    def button_subtract(self):
        first_number = self.e.get()
        self.math = "subtraction"
        self.fnum = int(first_number)
        self.e.delete(0,END)
        return

    def button_multiply(self):
        first_number = self.e.get()
        self.math = "multiplication"
        self.fnum = int(first_number)
        self.e.delete(0,END)
        return

    def button_divide(self):
        first_number = self.e.get()
        self.math = "division"
        self.fnum = int(first_number)
        self.e.delete(0,END)
        return

    def button_equal(self):
        second_number = self.e.get()
        self.e.delete(0,END)
        if self.math == "addition":
            self.e.insert(0, self.fnum + int(second_number))
        if self.math == "subtraction":
            self.e.insert(0, self.fnum - int(second_number))
        if self.math == "multiplication":
            self.e.insert(0, self.fnum * int(second_number))
        if self.math == "division":
            if int(second_number) == 0:
                self.e.insert(0, "Divison By Zero Error")
            else:
                self.e.insert(0, self.fnum / int(second_number))
        return

    def button_clear(self):
        self.e.delete(0,END)
        self.placeholder = ""
        self.fnum = 0
        return

    def button_click(self, number):
        current = self.e.get()
        self.e.delete(0,END)
        self.e.insert(0, str(current) + str(number))
        self.placeholder = str(current) + str(number)

    def place(self, button, x, y, c):
        button.grid(row = x, column = y, columnspan = c)
        
    def run(self):
        self.window.mainloop()
            
if __name__ == "__main__":
    calc = Calculator("ScientificCalculator")
    calc.run()
