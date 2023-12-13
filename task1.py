import tkinter as tk
import json
from datetime import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []
        self.load_tasks()

        # Entry for task input
        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, height=10, width=40)
        self.task_listbox.grid(row=1, column=0, padx=10, pady=5)

        # Buttons
        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.grid(row=2, column=0, padx=10, pady=5)

        remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        remove_button.grid(row=3, column=0, padx=10, pady=5)

        # Load tasks into the listbox
        self.update_task_listbox()

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=2)

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task['title']} - {task['date']}")

    def add_task(self):
        task_title = self.task_entry.get()
        if task_title:
            new_task = {"title": task_title, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            self.tasks.append(new_task)
            self.save_tasks()
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            self.update_task_listbox()
            print(f"Task removed: {removed_task['title']}")
        else:
            print("Select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
