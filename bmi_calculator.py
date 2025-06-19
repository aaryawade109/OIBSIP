# bmi_gui.py

import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Please enter positive numbers.")
            return

        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

        # Save to file
        with open("bmi_data.txt", "a") as file:
            file.write(f"Weight: {weight} kg, Height: {height} m, BMI: {bmi:.2f}, Category: {category}\n")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

def view_history():
    try:
        with open("bmi_data.txt", "r") as file:
            history = file.read()
        history_window = tk.Toplevel(root)
        history_window.title("BMI History")
        tk.Label(history_window, text=history, justify="left").pack(padx=10, pady=10)
    except FileNotFoundError:
        messagebox.showinfo("No History", "No history found yet!")

# GUI Setup
root = tk.Tk()
root.title("BMI Calculator")

# Weight input
tk.Label(root, text="Enter weight (kg):").grid(row=0, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1, padx=10, pady=10)

# Height input
tk.Label(root, text="Enter height (m):").grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1, padx=10, pady=10)

# Calculate button
calc_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calc_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="BMI: \nCategory: ")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# View history button
history_button = tk.Button(root, text="View History", command=view_history)
history_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
