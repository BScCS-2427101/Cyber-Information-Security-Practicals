# T101 Practical 3
# Message Authentication Code (MAC) using HMAC-SHA256
# GUI Version
import tkinter as tk
from tkinter import messagebox
import hashlib
import hmac
def generate_mac():
    message = entry_message.get()
    key = entry_key.get()
    if message == "" or key == "":
        messagebox.showerror("Error", "Enter Message and Secret Key")
        return
    mac = hmac.new(
        key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()
    entry_mac.delete(0, tk.END)
    entry_mac.insert(0, mac)
def verify_mac():
    message = entry_verify_message.get()
    key = entry_verify_key.get()
    received_mac = entry_verify_mac.get()
    new_mac = hmac.new(
        key.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()
    if hmac.compare_digest(new_mac, received_mac):
        lbl_result.config(
            text="Message Verified Successfully",
            fg="green"
        )
    else:
        lbl_result.config(
            text="Verification Failed",
            fg="red"
        )
root = tk.Tk()
root.title("Message Authentication Code (MAC)")
root.geometry("750x600")
root.configure(bg="#eef6ff")
title = tk.Label(
    root,
    text="Message Authentication Code (HMAC-SHA256)",
    font=("Arial", 18, "bold"),
    bg="#eef6ff",
    fg="navy"
)
title.pack(pady=15)
frame1 = tk.LabelFrame(
    root,
    text="Generate MAC",
    padx=15,
    pady=15,
    bg="#eef6ff"
)
frame1.pack(fill="x", padx=20)
tk.Label(frame1, text="Message", bg="#eef6ff").grid(row=0, column=0, pady=8)
entry_message = tk.Entry(frame1, width=55)
entry_message.grid(row=0, column=1)
tk.Label(frame1, text="Secret Key", bg="#eef6ff").grid(row=1, column=0, pady=8)
entry_key = tk.Entry(frame1, width=55, show="*")
entry_key.grid(row=1, column=1)
tk.Button(
    frame1,
    text="Generate MAC",
    command=generate_mac,
    bg="green",
    fg="white",
    width=18
).grid(row=2, column=1, pady=10)
tk.Label(frame1, text="Generated MAC", bg="#eef6ff").grid(row=3, column=0)
entry_mac = tk.Entry(frame1, width=70)
entry_mac.grid(row=3, column=1)
frame2 = tk.LabelFrame(
    root,
    text="Verify MAC",
    padx=15,
    pady=15,
    bg="#eef6ff"
)
frame2.pack(fill="x", padx=20, pady=15)
tk.Label(frame2, text="Message", bg="#eef6ff").grid(row=0, column=0, pady=8)
entry_verify_message = tk.Entry(frame2, width=55)
entry_verify_message.grid(row=0, column=1)
tk.Label(frame2, text="Secret Key", bg="#eef6ff").grid(row=1, column=0)
entry_verify_key = tk.Entry(frame2, width=55, show="*")
entry_verify_key.grid(row=1, column=1)
tk.Label(frame2, text="Received MAC", bg="#eef6ff").grid(row=2, column=0)
entry_verify_mac = tk.Entry(frame2, width=70)
entry_verify_mac.grid(row=2, column=1)
tk.Button(
    frame2,
    text="Verify MAC",
    command=verify_mac,
    bg="blue",
    fg="white",
    width=18
).grid(row=3, column=1, pady=10)
lbl_result = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#eef6ff"
)
lbl_result.pack(pady=20)
root.mainloop()
