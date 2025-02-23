from tkinter import *

class TruthTable:
    def __init__(self):
        self.win = Tk()
        self.win.title("")
        self.win.geometry("180x300")

        self.v = StringVar(self.win, "1")
        self.operators = {
            "AND": 1,
            "OR": 2,
            "NOT A": 3
        }

        self.user_answers = [IntVar() for _ in range(4)]
        self.correct_answers = []

        self.score = StringVar()
        self.score.set("Score: 0%")

        self.create_widgets()

    def create_widgets(self):
        Label(self.win, text="Choose Operator:").grid(row=0, column=0, sticky=W, pady=5)

        for index, (text, value) in enumerate(self.operators.items()):
            Radiobutton(self.win, text=text, variable=self.v, value=value).grid(row=index+1, column=0, sticky=W)

        Label(self.win, text="Enter 0 or 1 for each case:").grid(row=4, column=0, sticky=W, pady=5)

        truth_cases = [(1, 1), (1, 0), (0, 1), (0, 0)]
        for i, (a, b) in enumerate(truth_cases):
            Label(self.win, text=f"{a} {b if self.v.get() != '3' else ''} = ").grid(row=i+5, column=0, sticky=W)
            Entry(self.win, width=5, textvariable=self.user_answers[i]).grid(row=i+5, column=1)

        Button(self.win, text="Submit", command=self.evaluate).grid(row=10, column=0, pady=10)

        Label(self.win, textvariable=self.score).grid(row=11, column=0, pady=5)

    def evaluate(self):
        operator = int(self.v.get())
        truth_cases = [(1, 1), (1, 0), (0, 1), (0, 0)]

        if operator == 1: 
            self.correct_answers = [a & b for a, b in truth_cases]
        elif operator == 2: 
            self.correct_answers = [a | b for a, b in truth_cases]
        elif operator == 3: 
            self.correct_answers = [not a for a, _ in truth_cases]

        correct_count = sum(int(self.user_answers[i].get()) == self.correct_answers[i] for i in range(4))
        score_percentage = (correct_count / 4) * 100
        self.score.set(f"Score: {score_percentage}%")

def main():
    table = TruthTable()
    table.win.mainloop()

main()
