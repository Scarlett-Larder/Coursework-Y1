from tkinter import Tk, Frame, Label, Entry, Button, IntVar, StringVar, PhotoImage

class WhatToDo:
    
    def __init__(self):
        self.win = Tk()
        self.win.title("What to do today")
        self.win.geometry("300x200")

        self.main_frame = Frame(self.win)
        self.main_frame.pack(padx=10, pady=10)

        self.input = IntVar()
        self.what_to_do = StringVar()
        self.what_to_do.set("Please enter what temp it is!")

        self.image = PhotoImage()
    
    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):

        label_input = Label(
            self.main_frame,
            textvariable="Please enter what temp it is!"
        )
        label_input.pack()

        entry_input = Entry(
            self.main_frame,
            width=50,
            textvariable=self.input
        )
        entry_input.pack()

        button_deside = Button(
            self.main_frame,
            text="deside!",
            command=self.what_to_do_today
        )
        button_deside.pack()
        
        image_label = PhotoImage(
            self.main_frame
        )

    def what_to_do_today(self):
        temp = int(self.input.get())
        if temp > 25:
            print("A swim in the sea should be recomended")
        elif 10 <= temp <= 25:
            print("Shopping in Gunwharf Quays is a good idea")
        else:
            print("It’s best to watch a film at home")
        
def main():
    desider = WhatToDo()
    desider.run()

main()

# https://www.geeksforgeeks.org/how-to-add-an-image-in-tkinter/