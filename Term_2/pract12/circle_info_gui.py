from tkinter import Tk, Frame, Label, Entry, IntVar, Button, StringVar

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
        self.result1.set("0")
        self.result2.set("0")

    def run(self):
        self.create_widgets()
        self.win.mainloop()
    
    def create_widgets(self):
        entry_num1 = Entry(
            self.man_frame,
            width=
        )

def area_of_circle(radius):
    return math.pi * radius ** 2

def circumference_of_circle(radius):
    return 2 * math.pi * radius
