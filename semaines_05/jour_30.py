# Click Count App

import tkinter as tk

# Main Window
root = tk.Tk()
root.title("Click Count App")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Counter Variable
counter = 0

# Increment Counter Function
def increment_counter():
    global counter
    counter += 1
    counter_label.config(text=f"Clicks: {counter}")

# Reset Counter Function
def reset_counter():
    global counter
    counter = 0
    counter_label.config(text=f"Clicks: 0")

# Title Label
title_label = tk.Label(root, text="Click Count App", font=("Helvetica", 20), bg="#f0f0f0")

# Counter Label
counter_label = tk.Label(root, text="Clicks: 0", font=("Helvetica", 16), bg="#f0f0f0")

# Increment Button
increment_button = tk.Button(root, text="Click Me!", font=("Helvetica", 14), command=increment_counter, bg="#4CAF50", fg="white", padx=20, pady=10)
increment_button.pack(pady=20)

# Reset Button
reset_button = tk.Button(root, text="Reset", font=("Helvetica", 14), command=reset_counter, bg="#f44336", fg="white", padx=20, pady=10)
reset_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 14), command=root.quit, bg="#555555", fg="white", padx=20, pady=10)
exit_button.pack(pady=10)

# Run the Application
root.mainloop()