import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x500")

        self.tasks = []

        self.task_entry = ttk.Entry(root, font=("Helvetica", 14))
        self.task_entry.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.add_button = ttk.Button(root, text="Add Task", command=self.add_task, style="TButton")
        self.add_button.pack(padx=20, pady=10)

        self.task_list = tk.Listbox(root, font=("Helvetica", 14), selectbackground="green")
        self.task_list.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        self.remove_button = ttk.Button(root, text="Remove Task", command=self.remove_task, style="TButton")
        self.remove_button.pack(padx=20, pady=10)

        self.footer_label = ttk.Label(root, text="Made by Sai Jagadesh", font=("Helvetica", 15), foreground="blue")
        self.footer_label.pack(pady=10, side=tk.BOTTOM)
        self.footer_label.pack()

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 12))

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def remove_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            index = selected_task[0]
            del self.tasks[index]
            self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)

if __name__ == "__main__":
    print("Opening in a new window...")
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
    print("Closed Successfully :)")
