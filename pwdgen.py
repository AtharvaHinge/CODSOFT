import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length < 8:
        password_result.config(text="Password should be at least 8 characters long.", fg="red")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_result.config(text="Generated Password:", fg="black")
    generated_password.config(text=password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

length_label = tk.Label(root, text="Password Length:", bg="#f0f0f0")
length_label.pack()

length_entry = tk.Entry(root, width=20)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#0074d9", fg="white", activebackground="#0056a4", activeforeground="white")
generate_button.pack(pady=10)

password_result = tk.Label(root, text="", font=("Helvetica", 10, "italic"), bg="#f0f0f0")
password_result.pack()

generated_password = tk.Label(root, text="", font=("Courier", 14), bg="#f0f0f0", wraplength=300)
generated_password.pack(pady=10)

root.mainloop()