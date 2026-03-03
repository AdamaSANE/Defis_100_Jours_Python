# To-Do-List GUI
import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Functions
def add_task():
    task = entry_task.get()
    if task.strip():  # Check if task is not empty or only whitespace
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showerror("Input Error", "Task cannot be empty.")

def delete_task():
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showerror("Selection Error", "Please select a task to delete.")

def clear_tasks():
    listbox_tasks.delete(0, tk.END)

# Title Label
label_title = tk.Label(root, text="My To-Do List", font=("Helvetica", 16), bg="#f0f0f0")
label_title.pack(pady=10)

# Entry for new task
entry_task = tk.Entry(root, width=30, font=("Helvetica", 12)) 
entry_task.pack(pady=10)

# Buttons Frame
frame_buttons = tk.Frame(root, bg="#f0f0f0")  
frame_buttons.pack(pady=10)

button_add = tk.Button(frame_buttons, text="Add Task", command=add_task, bg="#4CAF50", fg="white", width=10)
button_add.grid(row=0, column=0, padx=5)

button_delete = tk.Button(frame_buttons, text="Delete Task", command=delete_task, bg="#f44336", fg="white", width=10)
button_delete.grid(row=0, column=1, padx=5)

button_clear = tk.Button(frame_buttons, text="Clear All", command=clear_tasks, bg="#2196F3", fg="white", width=10)
button_clear.grid(row=0, column=2, padx=5)

# Task Listbox with Scrollbar
frame_listbox = tk.Frame(root)
frame_listbox.pack(pady=10)

scrollbar_tasks = tk.Scrollbar(frame_listbox)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks = tk.Listbox(frame_listbox, width=50, height=15, yscrollcommand=scrollbar_tasks.set)
listbox_tasks.pack(pady=10)

scrollbar_tasks.config(command=listbox_tasks.yview)

# Exit Button
button_exit = tk.Button(root, text="Exit", command=root.quit, bg="#555555", fg="white", width=10)
button_exit.pack(pady=10)

# Start the GUI event loop
root.mainloop()
