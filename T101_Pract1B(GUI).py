#Design and implement algorithms to encrypt and decrypt messages using the Transposition (Rail Fence) Cipher in GUI.
import tkinter as tk
def encrypt_text():
    text = message_entry.get()
    if text == "":
        result_label.config(text="Please enter a message.")
        return
    first_row = ""
    second_row = ""
    for i in range(len(text)):
        if i % 2 == 0:
            first_row += text[i]
        else:
            second_row += text[i]
    encrypted = first_row + second_row
    result_label.config(text="Encrypted Message : " + encrypted)
def decrypt_text():
    text = message_entry.get()
    if text == "":
        result_label.config(text="Please enter a message.")
        return
    middle = (len(text) + 1) // 2
    first_row = text[:middle]
    second_row = text[middle:]
    original = ""
    for i in range(middle):
        original += first_row[i]

        if i < len(second_row):
            original += second_row[i]
    result_label.config(text="Decrypted Message : " + original)
def clear_all():
    message_entry.delete(0, tk.END)
    result_label.config(text="")
window = tk.Tk()
window.title("Transposition Cipher")
window.geometry("500x300")
window.resizable(False, False)
heading = tk.Label(
    window,
    text="Transposition Cipher (Rail Fence - 2 Rails)",
    font=("Arial", 14, "bold")
)
heading.pack(pady=10)
frame = tk.Frame(window)
frame.pack(pady=10)
message_label = tk.Label(frame, text="Enter Message :", font=("Arial", 11))
message_label.grid(row=0, column=0, padx=10, pady=10)
message_entry = tk.Entry(frame, width=35, font=("Arial", 11))
message_entry.grid(row=0, column=1)
button_frame = tk.Frame(window)
button_frame.pack(pady=10)
encrypt_button = tk.Button(
    button_frame,
    text="Encrypt",
    width=12,
    command=encrypt_text
)
encrypt_button.grid(row=0, column=0, padx=10)

decrypt_button = tk.Button(
    button_frame,
    text="Decrypt",
    width=12,
    command=decrypt_text
)
decrypt_button.grid(row=0, column=1, padx=10)
clear_button = tk.Button(
    button_frame,
    text="Clear",
    width=12,
    command=clear_all
)
clear_button.grid(row=0, column=2, padx=10)
result_title = tk.Label(
    window,
    text="Result",
    font=("Arial", 12, "bold")
)
result_title.pack(pady=(15, 5))
result_label = tk.Label(
    window,
    text="",
    width=50,
    height=3,
    relief="sunken",
    anchor="center",
    font=("Arial", 11)
)
result_label.pack(pady=5)
window.mainloop()
