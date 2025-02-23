from tkinter import Tk, Frame, Entry, Button, Label, StringVar, simpledialog
from backend import TaskList


class ToDoList:
    def __init__(self, task_list):
        self.task_list = task_list

        self.win = Tk()
        self.win.title("Task Manager")

        self.main_frame = Frame(self.win)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.new_task_message = StringVar()
        self.task_widgets = []

    def run(self):
        self.create_widgets()
        self.win.mainloop()

    def create_widgets(self):
        self.delete_all_task_widgets()

        task_entry = Entry(self.main_frame, textvariable=self.new_task_message)
        task_entry.grid(row=0, column=0, padx=5, pady=5)

        add_task_button = Button(
            self.main_frame, text="Add", command=self.add_task
        )
        add_task_button.grid(row=0, column=1, padx=5, pady=5)

        count = self.task_list.get_num_tasks()
        for i in range(count):
            task = self.task_list.get_task_message_by_index(i)
            task_label = Label(self.main_frame, text=task)
            task_label.grid(row=i+1, column=0, padx=5, pady=5)
            self.task_widgets.append(task_label)

            remove_task_button = Button(
                self.main_frame, text="Remove", command=lambda index=i: self.remove_task(index)
            )
            edit_task_button = Button(
                self.main_frame, text="Edit", command=lambda index=i: self.edit_task(index)
            )
            edit_task_button.grid(row=i+1, column=1, padx=5, pady=5)
            remove_task_button.grid(row=i+1, column=2, padx=5, pady=5)
            self.task_widgets.append(remove_task_button)

    def add_task(self):
        message = self.new_task_message.get()
        self.task_list.create_new_task(message)
        self.create_widgets()
        self.new_task_message.set("")
    
    def edit_task(self, index):
        # Prompt the user for a new task message using a dialog
        new_message = simpledialog.askstring("Edit Task", "Enter new task message:")
        if new_message:  # Only proceed if the user provides a new message
            self.task_list.set_task_message_at_index(index, new_message)
            self.create_widgets()

    def remove_task(self, index):
        self.task_list.remove_task_at_index(index)
        self.create_widgets()

    def delete_all_task_widgets(self):
        for widget in self.task_widgets:
            widget.destroy()
        self.task_widgets = []


def main():
    task_list = TaskList()
    app = ToDoList(task_list)
    app.run()

main()
