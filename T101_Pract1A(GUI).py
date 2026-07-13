# Design and implement algorithms to encrypt and decrypt messages using classical substitution techniques.(GUI)
import tkinter as tk
from tkinter import messagebox
def encrypt_message():
    message = message_box.get()
    key_text = key_box.get()
    if message == "" or key_text == "":
        messagebox.showwarning("Input Error", "Please enter the message and key.")
        return
    try:
        key = int(key_text)
    except ValueError:
        messagebox.showerror("Error", "Key must be a number.")
        return
    encrypted = ""
    for ch in message:
        if ch.isalpha():
            if ch.isupper():
                encrypted += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
            else:
                encrypted += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            encrypted += ch

    result.config(text=encrypted)
def decrypt_message():
    message = message_box.get()
    key_text = key_box.get()
    if message == "" or key_text == "":
        messagebox.showwarning("Input Error", "Please enter the message and key.")
        return
    try:
        key = int(key_text)
    except ValueError:
        messagebox.showerror("Error", "Key must be a number.")
        return
    decrypted = ""
    for ch in message:
        if ch.isalpha():
            if ch.isupper():
                decrypted += chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
            else:
                decrypted += chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
        else:
            decrypted += ch

    result.config(text=decrypted)
def clear_data():
    message_box.delete(0, tk.END)
    key_box.delete(0, tk.END)
    result.config(text="")
window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("450x320")
window.resizable(False, False)
window.configure(bg="#f4f4f4")
title = tk.Label(
    window,
    text="Classical Substitution Cipher",
    font=("Arial", 16, "bold"),
    bg="#f4f4f4"
)
title.pack(pady=15)
tk.Label(
    window,
    text="Enter Message",
    font=("Arial", 11),
    bg="#f4f4f4"
).pack()

message_box = tk.Entry(window, font=("Arial", 12), width=35)
message_box.pack(pady=5)
tk.Label(
    window,
    text="Enter Key",
    font=("Arial", 11),
    bg="#f4f4f4"
).pack()
key_box = tk.Entry(window, font=("Arial", 12), width=10)
key_box.pack(pady=5)
button_frame = tk.Frame(window, bg="#f4f4f4")
button_frame.pack(pady=15)
encrypt_btn = tk.Button(
    button_frame,
    text="Encrypt",
    width=10,
    command=encrypt_message
)
encrypt_btn.grid(row=0, column=0, padx=8)
decrypt_btn = tk.Button(
    button_frame,
    text="Decrypt",
    width=10,
    command=decrypt_message
)
decrypt_btn.grid(row=0, column=1, padx=8)
clear_btn = tk.Button(
    button_frame,
    text="Clear",
    width=10,
    command=clear_data
)
clear_btn.grid(row=0, column=2, padx=8)
tk.Label(
    window,
    text="Result",
    font=("Arial", 11, "bold"),
    bg="#f4f4f4"
).pack()
result = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    fg="blue",
    bg="white",
    width=35,
    height=2,
    relief="sunken"
)
result.pack(pady=8)
window.mainloop()
