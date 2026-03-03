# Smple Login System
import tkinter as tk  
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Simple Login System")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Predefined Credentials
USER_CREDENTIALS = {
    "admin": "admin123",
    "user": "user123"
}

# Title Label
title_label = tk.Label(root, text="Login", font=("Arial", 20), bg="#f0f0f0")
title_label.pack(pady=20)

# Username Label and Entry
username_label = tk.Label(root, text="Username:", font=("Arial", 14), bg="#f0f0f0")
username_label.pack(pady=5)
username_entry = tk.Entry(root, font=("Arial", 14))
username_entry.pack(pady=5)

# Password Label and Entry
password_label = tk.Label(root, text="Password:", font=("Arial", 14), bg="#f0f0f0")
password_label.pack(pady=5)
password_entry = tk.Entry(root, font=("Arial", 14), show="*")
password_entry.pack(pady=5)

# Login Function
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
        messagebox.showinfo("Login Successful", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Clear Function
def clear():
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Login Button
login_button = tk.Button(root, text="Login", font=("Arial", 14), command=login)
login_button.pack(pady=10)

# Clear Button
clear_button = tk.Button(root, text="Clear", font=("Arial", 14), command=clear)
clear_button.pack(pady=5)

# Exit Button
exit_button = tk.Button(root, text="Exit", font=("Arial", 14), command=root.destroy)
exit_button.pack(pady=5)

# Run the Application
root.mainloop()