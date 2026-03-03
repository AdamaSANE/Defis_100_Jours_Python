# Expense Tracker App(GUI Capstone Project)

import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

# Expense Tracker App

# File to storing expenses
EXPENSE_FILE = 'expenses.csv'

# Create the main application window
root = tk.Tk()
root.title("Expense Tracker App")
root.geometry("600x600")
root.configure(bg="#f0f4c3")

# Expense Data List
expenses = []

# Load Existing Expenses from CSV
def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                expenses.append(row)
                expense_listbox.insert(tk.END, f"{row[0]} | ${row[1]} | {row[2]}")  

# Save Expense to CSV
def save_expense(expense):
    with open(EXPENSE_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for exp in expenses:
            writer.writerow(exp)

# Add Expense Function
def add_expense():
    category = category_var.get()
    amount = amount_entry.get()
    description = description_entry.get()

    if not amount.isdigit() or not category or not description:
        messagebox.showerror("Input Error", "Please enter valid data for all fields.")
        return
    expenses.append([category, amount, description])
    expense_listbox.insert(tk.END, f"{category} | ${amount} | {description}")
    calculate_total()
    clear_inputs()
    save_expense()

# Delete Selected Expense
def delete_expense():
    selected_index = expense_listbox.curselection()
    if not selected_index:
        messagebox.showerror("Selection Error", "Please select an expense to delete.")
        return
    index = selected_index[0]
    del expenses[index]
    expense_listbox.delete(index)
    calculate_total()
    save_expense()

# Clear Input Fields
def clear_inputs():
    category_var.set('Select Category')
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

# Calculate Total Expenses
def calculate_total():
    total = sum(float(expense[1]) for expense in expenses)
    total_label.config(text=f"Total Expenses: ${total:.2f}")

# Clear All Expenses
def clear_all_expenses():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all expenses?"):
        expenses.clear()
        expense_listbox.delete(0, tk.END)
        calculate_total()
        save_expense()

# --- GUI Layout ---
# Title Label
title_label = tk.Label(root, text="Expense Tracker App", font=("Helvetica", 18, "bold"), bg="#f0f4c3")
title_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#f0f4c3")  
input_frame.pack(pady=10)

# Category 
category_label = tk.Label(input_frame, text="Category:", font=("Helvetica", 12), bg="#f0f4c3")
category_label.grid(row=0, column=0, padx=5, pady=5)
category_var = tk.StringVar(value='Select Category')
category_dropdown = ttk.Combobox(input_frame, textvariable=category_var, values=['Food', 'Transport', 'Entertainment', 'Other'])
category_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Amount
amount_label = tk.Label(input_frame, text="Amount ($):", font=("Helvetica", 12), bg="#f0f4c3")
amount_label.grid(row=1, column=0, padx=5, pady=5)
amount_entry = tk.Entry(input_frame)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

# Description
description_label = tk.Label(input_frame, text="Description:", font=("Helvetica", 12), bg="#f0f4c3")
description_label.grid(row=2, column=0, padx=5, pady=5)
description_entry = tk.Entry(input_frame)
description_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons Frame
button_frame = tk.Frame(root, bg="#f0f4c3") 
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Expense", command=add_expense, bg="#4caf50", fg="white")
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Selected", command=delete_expense, bg="#f44336", fg="white")
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear All", command=clear_all_expenses, bg="#740b03", fg="white")
clear_button.grid(row=0, column=2, padx=5)

# Expense Listbox with Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(pady=10)

expense_listbox = tk.Listbox(list_frame, width=50, height=15)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

expense_listbox = tk.Listbox(list_frame, width=50, height=15, yscrollcommand=scrollbar.set)
expense_listbox.pack()

scrollbar.config(command=expense_listbox.yview)

# Total Label
total_label = tk.Label(root, text="Total Expenses: $0.00", font=("Helvetica", 14), bg="#f0f4c3")
total_label.pack(pady=10)

# Load existing expenses and calculate total
load_expenses()
calculate_total()

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="#9e9e9e", fg="white")
exit_button.pack(pady=10)

# Start the main event loop
root.mainloop()