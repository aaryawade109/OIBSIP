# password_generator_gui.py

import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Input Error", "Length must be positive.")
            return

        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        characters = ''
        if use_letters:
            characters += string.ascii_letters
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Input Error", "Select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for length.")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first!")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters", variable=letters_var).grid(row=1, column=0, sticky="w", padx=10)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, column=0, sticky="w", padx=10)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, sticky="w", padx=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

password_entry = tk.Entry(root, width=40)
password_entry.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
