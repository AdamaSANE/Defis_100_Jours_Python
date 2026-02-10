# BMI Calculator
import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Title label
title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 24), bg="#f0f0f0")
title_label.pack(pady=20)

# Weight input
weight_label = tk.Label(root, text="Enter your Weight (kg):", font=("Arial", 14), bg="#f0f0f0")
weight_label.pack()
weight_entry = tk.Entry(root, font=("Arial", 14), width=10)
weight_entry.pack(pady=10)

# Height input
height_label = tk.Label(root, text="Enter your Height (cm):", font=("Arial", 14), bg="#f0f0f0")
height_label.pack() 
height_entry = tk.Entry(root, font=("Arial", 14), width=10)
height_entry.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
result_label.pack(pady=20)

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive numbers.")
        bmi = weight / ((height / 100) ** 2)
        status = ""
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi < 24.9:
            status = "Normal weight"
        elif 25 <= bmi < 29.9:
            status = "Overweight"
        else:
            status = "Obesity"
        result_label.config(text=f"Your BMI is: {bmi:.2f}\n ({status})", fg="green")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

# Calculate button
calculate_button = tk.Button(root, text="Calculate BMI", font=("Arial", 14), command=calculate_bmi, bg="#4CAF50", fg="white")
calculate_button.pack(pady=10)

# Button reset
reset_button = tk.Button(root, text="Reset", font=("Arial", 14), command=lambda: [weight_entry.delete(0, tk.END), height_entry.delete(0, tk.END), result_label.config(text="")], bg="#f44336", fg="white")
reset_button.pack(pady=10)

# Run the application
root.mainloop()