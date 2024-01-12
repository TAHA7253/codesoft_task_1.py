import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManager:
  def __init__(self):
      self.root = tk.Tk()
      self.root.title("TO DO LIST")
      self.tasks = []
      self.task_var = tk.StringVar()
      self.task_entry = tk.Entry(self.root, textvariable=self.task_var, font=("Arial", 14))
      self.task_entry.grid(row=0, column=0, padx=10, pady=10)
      self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, font=("Arial", 14), bg= 'green')
      self.add_button.grid(row=1, column=0, padx=10, pady=10)
      self.edit_button = tk.Button(self.root, text="Edit Task", command=self.edit_task, font=("Arial", 14), bg='cyan')
      self.edit_button.grid(row=2, column=0, padx=10, pady=10)
      self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, font=("Arial", 14), bg='red')
      self.delete_button.grid(row=3, column=0, padx=10, pady=10)
      self.task_listbox = tk.Listbox(self.root, font=("Arial", 14))
      self.task_listbox.grid(row=0, column=1, rowspan=4, padx=10, pady=10)

  def add_task(self):
      task = self.task_var.get()
      if task == "":
          messagebox.showinfo("Error", "Please enter a task.")
      else:
          task_number = str(len(self.tasks) + 1) + ". " + task
          self.tasks.append(task_number)
          self.task_listbox.insert(tk.END, task_number)
          self.task_var.set("")

  def edit_task(self):
      selected_task = self.task_listbox.curselection()
      if len(selected_task) > 0:
          task_index = selected_task[0]
          new_task = simpledialog.askstring("Edit Task", "Enter the new task:")
          if new_task:
              new_task_number = str(task_index + 1) + ". " + new_task
              self.tasks[task_index] = new_task_number
              self.task_listbox.delete(task_index)
              self.task_listbox.insert(task_index, new_task_number)
      else:
          messagebox.showinfo("Error", "No task selected.")

  def delete_task(self):
      selected_task = self.task_listbox.curselection()
      if len(selected_task) > 0:
          task_index = selected_task[0]
          del self.tasks[task_index]
          self.task_listbox.delete(task_index)
          # Update serial numbers
          for i, task in enumerate(self.tasks):
              task_number, task_text = task.split(". ", 1)
              new_task = str(i+1) + ". " + task_text
              self.tasks[i] = new_task
              self.task_listbox.delete(i)
              self.task_listbox.insert(i, new_task)
      else:
          messagebox.showinfo("Error", "No task selected.")

  def run(self):
      self.root.mainloop()

if __name__ == "__main__":
  app = TaskManager()
  app.run()
