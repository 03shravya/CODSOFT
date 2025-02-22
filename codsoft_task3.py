import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip
import time


# Function to generate password
def generate_password():
    password_entry.delete(0, tk.END)
    password_entry.insert(0, "Generating... ⏳")
    root.update_idletasks()
    time.sleep(0.5)

    length = length_var.get()

    if not length.isdigit() or int(length) <= 0:
        messagebox.showwarning("⚠️ Warning", "Please enter a valid password length!")
        password_entry.delete(0, tk.END)
        return

    length = int(length)
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_numbers = number_var.get()
    use_symbols = symbol_var.get()

    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("⚠️ Warning", "Please select at least one character type!")
        password_entry.delete(0, tk.END)
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    update_strength_label(password)


# Function to copy password to clipboard
def copy_to_clipboard():
    password = password_entry.get()
    if password and password != "Generating... ⏳":
        pyperclip.copy(password)
        messagebox.showinfo("✅ Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("⚠️ Warning", "No password to copy!")


# Function to check password strength
def update_strength_label(password):
    strength_label.config(fg="black")
    if len(password) < 6:
        strength_label.config(text="🔴 Weak", fg="red")
    elif 6 <= len(password) < 10:
        strength_label.config(text="🟡 Medium", fg="orange")
    else:
        strength_label.config(text="🟢 Strong", fg="green")


# GUI Setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("550x650")
root.config(bg="#2C3E50")  # Dark background

# Title Label
tk.Label(root, text="🔒 Secure Password Generator", font=("Arial", 20, "bold"), bg="#2C3E50", fg="white").pack(pady=20)

# Password Length
tk.Label(root, text="🔢 Password Length:", bg="#2C3E50", fg="white", font=("Arial", 14, "bold")).pack(pady=5)
length_var = tk.StringVar()
length_entry = tk.Entry(root, textvariable=length_var, width=5, font=("Arial", 16), bg="white", fg="black",
                        justify="center")
length_entry.pack(pady=5)

# Checkbox Styling (Large)
check_font = ("Arial", 14, "bold")
check_bg = "#34495E"  # Dark gray-blue
check_fg = "white"

# Options for password strength (Now defaulting to unchecked)
upper_var = tk.BooleanVar(value=False)
lower_var = tk.BooleanVar(value=False)
number_var = tk.BooleanVar(value=False)
symbol_var = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="🔠 Include Uppercase", variable=upper_var, font=check_font, bg=check_bg, fg=check_fg,
               selectcolor=check_bg, padx=10, pady=5).pack()
tk.Checkbutton(root, text="🔡 Include Lowercase", variable=lower_var, font=check_font, bg=check_bg, fg=check_fg,
               selectcolor=check_bg, padx=10, pady=5).pack()
tk.Checkbutton(root, text="🔢 Include Numbers", variable=number_var, font=check_font, bg=check_bg, fg=check_fg,
               selectcolor=check_bg, padx=10, pady=5).pack()
tk.Checkbutton(root, text="🔣 Include Symbols", variable=symbol_var, font=check_font, bg=check_bg, fg=check_fg,
               selectcolor=check_bg, padx=10, pady=5).pack()

# Generate Button
generate_btn = tk.Button(root, text="🔄 Generate Password", command=generate_password, bg="#27AE60", fg="white",
                         font=("Arial", 16, "bold"), padx=20, pady=12)
generate_btn.pack(pady=20)

# Password Entry
password_entry = tk.Entry(root, font=("Arial", 18, "bold"), width=30, justify="center", bg="white", fg="black",
                          relief="solid", borderwidth=3)
password_entry.pack(pady=10)

# Strength Label
strength_label = tk.Label(root, text="🟡 Strength: TBD", font=("Arial", 14, "bold"), bg="#2C3E50", fg="white")
strength_label.pack(pady=10)

# Copy Button
copy_btn = tk.Button(root, text="📋 Copy to Clipboard", command=copy_to_clipboard, bg="#2980B9", fg="white",
                     font=("Arial", 16, "bold"), padx=20, pady=12)
copy_btn.pack(pady=10)

# Footer
tk.Label(root, text="🔑 Secure & Random Passwords Every Time!", font=("Arial", 12, "italic"), bg="#2C3E50",
         fg="gray").pack(pady=20)

# Run GUI
root.mainloop()

