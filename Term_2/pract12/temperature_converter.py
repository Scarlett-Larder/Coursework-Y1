from tkinter import Tk, Frame, Label, Entry, Button, IntVar, StringVar

class TempConvert:

    def __init__(self):
        self.win = Tk()
        self.win.title("TemperatureConverter")
        self.win.geometry("300x200")

        self.main_frame = Frame(self.win)
        self.main_frame.pack(padx=10, pady=10)

        self.fahren = IntVar()
        self.celsius = IntVar()
        
    def run(self):
        self.create_widgets()
        self.win.mainloop()
    
    def create_widgets(self):

        label_fahren = Label(
            self.main_frame,
            text="Fahrenheit"
        )
        label_fahren.pack()

        entry_fahren = Entry(
            self.main_frame,
            width=50,
            textvariable=self.fahren
        )
        entry_fahren.pack()

        label_celsius = Label(
            self.main_frame,
            text="Celsius"
        )
        label_celsius.pack()

        entry_celsius = Entry(
            self.main_frame,
            width=50,
            textvariable=self.celsius
        )
        entry_celsius.pack()

        button_fahren = Button(
            self.main_frame,
            text="Convert to Fahrenheit",
            command=self.convert_fahren
        )
        button_fahren.pack(side="left")

        button_celsius = Button(
            self.main_frame,
            text="Convert to Celsius",
            command=self.convert_celsius
        )
        button_celsius.pack(side="right")

    
    def convert_fahren(self):
         
        cel = int(self.celsius.get())
        fah = (cel * 1.8) + 32
        self.fahren.set(fah)



    def convert_celsius(self):
        
        fah = int(self.fahren.get())
        cel = (fah - 32) / 1.8
        self.celsius.set(cel)

def main():
    converter = TempConvert()
    converter.run()

main()