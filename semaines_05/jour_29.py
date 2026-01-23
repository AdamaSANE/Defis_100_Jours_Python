# Simple GUI App
import tkinter as tk

# Main window
root = tk.Tk()
root.title("Simple GUI App")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Label
label = tk.Label(root, text="Welcome to the Simple GUI App!", bg="#f0f0f0", font=("Arial", 16))
label.pack(pady=20)

# Name Entry
name_label = tk.Label(root, text="Enter your name:", bg="#f0f0f0", font=("Arial", 12))
name_label.pack(pady=5)

name_entry = tk.Entry(root, font=("Arial", 12), width=30)
name_entry.pack(pady=10)

# Greeting Function
def greet():
    name = name_entry.get()
    if name:
        greeting_label.config(text=f"Hello, {name}!", fg="green")
    else:
        greeting_label.config(text="Please enter your name.", fg="red")

# Reset Function
def reset():
    name_entry.delete(0, tk.END)
    greeting_label.config(text="")

# Greet Button
greet_button = tk.Button(root, text="Greet Me", command=greet, font=("Arial", 12), bg="#4CAF50", fg="white")
greet_button.pack(pady=10)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=reset, font=("Arial", 12), bg="#f44336", fg="white")
reset_button.pack(pady=5)

# Greeting Label
greeting_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 14))
greeting_label.pack(pady=20)

# Run the application
root.mainloop()