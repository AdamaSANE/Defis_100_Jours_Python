# Drawing Pad App

import tkinter as tk
from tkinter import colorchooser

# Main Window
root = tk.Tk()
root.title("Drawing Pad") 
root.geometry("800x600")
root.configure(bg="white")

# Global Variables
current_color = "black"
current_thickness = 2

# Create Canvas
canvas = tk.Canvas(root, bg="white", width=800, height=500, bd=2)
canvas.pack(pady=20)

# Drawing Function
def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(x - current_thickness, y - current_thickness, x + current_thickness, y + current_thickness, fill=current_color, outline=current_color) 

# Clear Canvas Function
def clear_canvas():
    canvas.delete("all")

# Change Color Function
def change_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color

# Change Thickness Function
def change_thickness(value):
    global current_thickness
    current_thickness = int(value)

# Bind Drawing Function to Mouse Drag
canvas.bind("<B1-Motion>", draw)

# Control Panel
control_frame = tk.Frame(root, bg="white")
control_frame.pack(pady=10)

# Color Button
color_button = tk.Button(control_frame, text="Change Color", command=change_color, bg="lightgray", fg="black", font=("Arial", 12, "bold"))
color_button.grid(row=0, column=0, padx=10)

# Clear Button
clear_button = tk.Button(control_frame, text="Clear Canvas", command=clear_canvas, bg="lightgray", fg="black", font=("Arial", 12, "bold"))
clear_button.grid(row=0, column=1, padx=10)

# Thickness Control
thickness_label = tk.Label(control_frame, text=f"Thickness: {current_thickness}", font=("Arial", 12, "bold"), bg="white")
thickness_label.grid(row=0, column=2, padx=10)

thickness_slider = tk.Scale(control_frame, from_=1, to=10, orient=tk.HORIZONTAL, command=lambda value: [change_thickness(value), thickness_label.config(text=f"Thickness: {value}")], bg="white")
thickness_slider.set(current_thickness)

# Start the Application
root.mainloop()