import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.setup_ui()

    def setup_ui(self):
        self.frame_tasks = tk.Frame(self.root)
        self.frame_tasks.pack()

        self.listbox_tasks = tk.Listbox(self.frame_tasks, height=10, width=50, selectmode=tk.SINGLE)
        self.listbox_tasks.pack(side=tk.LEFT)

        self.scrollbar_tasks = tk.Scrollbar(self.frame_tasks)
        self.scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox_tasks.config(yscrollcommand=self.scrollbar_tasks.set)
        self.scrollbar_tasks.config(command=self.listbox_tasks.yview)

        self.listbox_tasks.bind("<<ListboxSelect>>", self.update_mark_button_state)

        self.entry_task = tk.Entry(self.root, width=50)
        self.entry_task.pack()

        self.button_add_task = tk.Button(self.root, text="Add Task", width=48, command=self.add_task)
        self.button_add_task.pack()

        self.button_delete_task = tk.Button(self.root, text="Delete Task", width=48, command=self.delete_task)
        self.button_delete_task.pack()

        self.button_toggle_completed = tk.Button(self.root, text="Mark Task", width=48, command=self.toggle_completed)
        self.button_toggle_completed.pack()

        self.button_edit_task = tk.Button(self.root, text="Edit Task", width=48, command=self.edit_task)
        self.button_edit_task.pack()

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.listbox_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning(title="Warning!", message="You must enter a task.")

    def delete_task(self):
        try:
            task_index = self.listbox_tasks.curselection()[0]
            task_text = self.listbox_tasks.get(task_index)
            
            if task_text.endswith(" ✔"):
                self.button_toggle_completed.config(text="Mark task")
            
            self.listbox_tasks.delete(task_index)
        except IndexError:
            messagebox.showwarning(title="Warning!", message="You must select a task.")

    def toggle_completed(self):
        try:
            task_index = self.listbox_tasks.curselection()[0]
            task_text = self.listbox_tasks.get(task_index)
            
            if task_text.endswith(" ✔"):
                updated_task = task_text[:-2]
                self.button_toggle_completed.config(text="Mark task")
            else:
                updated_task = task_text + " ✔"
                self.button_toggle_completed.config(text="Unmark task")
            
            self.listbox_tasks.delete(task_index)
            self.listbox_tasks.insert(task_index, updated_task)
        except IndexError:
            pass

    def edit_task(self):
        try:
            task_index = self.listbox_tasks.curselection()[0]
            current_task = self.listbox_tasks.get(task_index)
            
            if current_task.endswith(" ✔"):
                current_task = current_task[:-2]
            
            edit_window = tk.Toplevel(self.root)
            edit_window.title("Edit Task")
            
            entry_edit = tk.Entry(edit_window, width=50)
            entry_edit.pack()
            entry_edit.insert(0, current_task)
            
            def save_edit():
                updated_task = entry_edit.get()
                if updated_task:
                    self.listbox_tasks.delete(task_index)
                    self.listbox_tasks.insert(task_index, updated_task)
                    edit_window.destroy()
                    if updated_task.endswith(" ✔"):
                        self.button_toggle_completed.config(text="Unmark task")
                    else:
                        self.button_toggle_completed.config(text="Mark task")
                else:
                    messagebox.showwarning(title="Warning!", message="You must enter a task.")
            
            button_save_edit = tk.Button(edit_window, text="Save Edit", width=48, command=save_edit)
            button_save_edit.pack()

        except IndexError:
            messagebox.showwarning(title="Warning!", message="You must select a task.")

    def update_mark_button_state(self, event):
        try:
            task_index = self.listbox_tasks.curselection()[0]
            task_text = self.listbox_tasks.get(task_index)
            if task_text.endswith(" ✔"):
                self.button_toggle_completed.config(text="Unmark task")
            else:
                self.button_toggle_completed.config(text="Mark task")
        except IndexError:
            pass

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()