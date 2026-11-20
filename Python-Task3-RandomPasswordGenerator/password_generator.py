
import tkinter as tk
from tkinter import messagebox
import secrets
import string


def generate_password(length, selected_types):
    characters = ""
    password = []

    pools = {
        "uppercase": string.ascii_uppercase,
        "lowercase": string.ascii_lowercase,
        "numbers": string.digits,
        "symbols": string.punctuation
    }

    for name, pool in pools.items():
        if name in selected_types:
            characters += pool
            password.append(secrets.choice(pool))

    for _ in range(length - len(password)):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def create_password():
    try:
        length = int(length_entry.get())

        if length < 8:
            messagebox.showwarning(
                "Invalid Length",
                "Password length must be at least 8."
            )
            return

        if length > 128:
            messagebox.showwarning(
                "Invalid Length",
                "Maximum password length is 128."
            )
            return

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number."
        )
        return

    selected = [
        name for name, variable in options.items()
        if variable.get()
    ]

    if len(selected) < 2:
        messagebox.showwarning(
            "Selection Required",
            "Select at least 2 character types."
        )
        return

    password = generate_password(length, selected)

    password_entry.config(show="")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


def copy_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning(
            "No Password",
            "Generate a password first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")


def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_button.config(text="Hide")
    else:
        password_entry.config(show="*")
        show_button.config(text="Show")


# Main Window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("480x570")
root.resizable(False, False)
root.configure(bg="#14243B")

title = tk.Label(
    root,
    text="PASSWORD GENERATOR",
    font=("Arial", 20, "bold"),
    bg="#14243B",
    fg="white"
)
title.pack(pady=(30, 8))

subtitle = tk.Label(
    root,
    text="Create a secure random password",
    font=("Arial", 10),
    bg="#14243B",
    fg="#CBD5E1"
)
subtitle.pack(pady=5)

# Password Length
tk.Label(
    root,
    text="Password Length (8-128)",
    font=("Arial", 11, "bold"),
    bg="#14243B",
    fg="white"
).pack(pady=(25, 8))

length_entry = tk.Entry(
    root,
    font=("Arial", 13),
    justify="center",
    width=12
)
length_entry.pack(ipady=6)
length_entry.insert(0, "16")

# Character Options
tk.Label(
    root,
    text="Select Character Types",
    font=("Arial", 11, "bold"),
    bg="#14243B",
    fg="white"
).pack(pady=(25, 10))

options_frame = tk.Frame(root, bg="#14243B")
options_frame.pack()

options = {}

choices = [
    ("uppercase", "Uppercase (A-Z)"),
    ("lowercase", "Lowercase (a-z)"),
    ("numbers", "Numbers (0-9)"),
    ("symbols", "Symbols (!@#$)")
]

for name, label in choices:
    variable = tk.BooleanVar(value=True)
    options[name] = variable

    tk.Checkbutton(
        options_frame,
        text=label,
        variable=variable,
        font=("Arial", 10),
        bg="#14243B",
        fg="white",
        selectcolor="#263B55",
        activebackground="#14243B",
        activeforeground="white"
    ).pack(anchor="w", pady=3)

# Generate Button
tk.Button(
    root,
    text="GENERATE PASSWORD",
    font=("Arial", 11, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    activeforeground="white",
    cursor="hand2",
    command=create_password
).pack(pady=22, ipadx=20, ipady=8)

# Password Output
password_entry = tk.Entry(
    root,
    font=("Consolas", 12),
    justify="center",
    width=34,
    show="*"
)
password_entry.pack(ipady=8)

# Show / Hide
show_button = tk.Button(
    root,
    text="Show",
    command=toggle_password,
    bg="#334155",
    fg="white",
    cursor="hand2"
)
show_button.pack(pady=7)

# Copy Button
tk.Button(
    root,
    text="COPY PASSWORD",
    font=("Arial", 10, "bold"),
    bg="#16A34A",
    fg="white",
    activebackground="#15803D",
    activeforeground="white",
    cursor="hand2",
    command=copy_password
).pack(pady=8, ipadx=15, ipady=6)

footer = tk.Label(
    root,
    text="Powered by Python secrets module",
    font=("Arial", 9),
    bg="#14243B",
    fg="#94A3B8"
)
footer.pack(side="bottom", pady=15)

root.mainloop()
