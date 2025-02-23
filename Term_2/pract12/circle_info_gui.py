from tkinter import Tk, Frame, Label, Entry, IntVar, Button, StringVar
import math

class CircleInfo:

    def __init__(self):
        self.win = Tk()
        self.win.title("Circle Info")
        self.win.geometry("300x200")

        self.main_frame = Frame(self.win)
        self.main_frame.pack(padx=10, pady=10)

        self.num1 = IntVar()

        self.result1 = StringVar()
        self.result2 = StringVar()
        self.result1.set("Area: 0")
        self.result2.set("Circ: 0")

    def run(self):
        self.create_widgets()
        self.win.mainloop()
    
    def create_widgets(self):

        label_num1 = Label(
            self.main_frame,
            text="Number 1: "
        )
        label_num1.pack()

        entry_num1 = Entry(
            self.main_frame,
            width=20,
            textvariable=self.num1
        )
        entry_num1.pack()

        label_result1 = Label(
            self.main_frame,
            width=20,
            textvariable=self.result1
        )
        label_result1.pack()

        label_result2 = Label(
            self.main_frame,
            width=20,
            textvariable=self.result2
        )
        label_result2.pack()

        button_mult = Button(
            self.main_frame,
            text="Calc",
            command=self.calculate
        )
        button_mult.pack(side="left")
    
    def calculate(self):
        print("Calculate!")

        val = int(self.num1.get())
        result1 = math.pi * val ** 2
        result2 = 2 * math.pi * val

        self.result1.set(f"Area: {result1}")
        self.result2.set(f"Circ: {result2}")


def main():
    calc = CircleInfo()
    calc.run()


main()

