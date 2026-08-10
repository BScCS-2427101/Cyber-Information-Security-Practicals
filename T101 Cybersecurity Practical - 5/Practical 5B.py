import tkinter as tk
from tkinter import messagebox
import math

# ---------------- PRIME NUMBER CHECK ----------------
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# ---------------- DIFFIE-HELLMAN CALCULATION ----------------
def calculate_keys():
    try:
        # Get values from GUI
        p = int(p_entry.get())
        g = int(g_entry.get())
        user1_private = int(user1_private_entry.get())
        user2_private = int(user2_private_entry.get())
        # Validate p
        if not is_prime(p):
            messagebox.showerror(
                "Invalid Input",
                "p must be a prime number."
            )
            return
        # Validate g
        if g <= 1 or g >= p:
            messagebox.showerror(
                "Invalid Input",
                "g must satisfy 1 < g < p."
            )
            return
        # Validate private keys
        if user1_private <= 0:
            messagebox.showerror(
                "Invalid Input",
                "User 1 private key must be greater than 0."
            )
            return
        if user2_private <= 0:
            messagebox.showerror(
                "Invalid Input",
                "User 2 private key must be greater than 0."
            )
            return

        # ---------------- PUBLIC KEYS ----------------
        user1_public = pow(
            g,
            user1_private,
            p
        )
        user2_public = pow(
            g,
            user2_private,
            p
        )

        # ---------------- SHARED SECRET KEYS ----------------
        user1_shared_secret = pow(
            user2_public,
            user1_private,
            p
        )
        user2_shared_secret = pow(
            user1_public,
            user2_private,
            p
        )

        # ---------------- DISPLAY OUTPUT ----------------
        output_text.delete(
            "1.0",
            tk.END
        )
        output_text.insert(
            tk.END,
            "=" * 65 + "\n"
        )
        output_text.insert(
            tk.END,
            "       DIFFIE-HELLMAN KEY EXCHANGE RESULT\n"
        )
        output_text.insert(
            tk.END,
            "=" * 65 + "\n\n"
        )
        output_text.insert(
            tk.END,
            "PUBLIC PARAMETERS\n"
        )
        output_text.insert(
            tk.END,
            "-" * 65 + "\n"
        )
        output_text.insert(
            tk.END,
            f"Prime Number (p): {p}\n"
        )
        output_text.insert(
            tk.END,
            f"Generator (g)  : {g}\n\n"
        )
        output_text.insert(
            tk.END,
            "PRIVATE KEYS\n"
        )
        output_text.insert(
            tk.END,
            "-" * 65 + "\n"
        )
        output_text.insert(
            tk.END,
            f"User 1 Private Key: {user1_private}\n"
        )
        output_text.insert(
            tk.END,
            f"User 2 Private Key: {user2_private}\n\n"
        )
        output_text.insert(
            tk.END,
            "PUBLIC KEY GENERATION\n"
        )

        output_text.insert(
            tk.END,
            "-" * 65 + "\n"
        )
        output_text.insert(
            tk.END,
            f"User 1 Public Key = g^User1_Private mod p\n"
        )

        output_text.insert(
            tk.END,
            f"User 1 Public Key = {user1_public}\n\n"
        )
        output_text.insert(
            tk.END,
            f"User 2 Public Key = g^User2_Private mod p\n"
        )
        output_text.insert(
            tk.END,
            f"User 2 Public Key = {user2_public}\n\n"
        )
        output_text.insert(
            tk.END,
            "SHARED SECRET KEY CALCULATION\n"
        )
        output_text.insert(
            tk.END,
            "-" * 65 + "\n"
        )
        output_text.insert(
            tk.END,
            "User 1 calculates:\n"
        )
        output_text.insert(
            tk.END,
            "Shared Key = User 2 Public Key ^ User 1 Private Key mod p\n"
        )
        output_text.insert(
            tk.END,
            f"User 1 Shared Secret Key = {user1_shared_secret}\n\n"
        )
        output_text.insert(
            tk.END,
            "User 2 calculates:\n"
        )
        output_text.insert(
            tk.END,
            "Shared Key = User 1 Public Key ^ User 2 Private Key mod p\n"
        )
        output_text.insert(
            tk.END,
            f"User 2 Shared Secret Key = {user2_shared_secret}\n\n"
        )
        output_text.insert(
            tk.END,
            "KEY VERIFICATION\n"
        )
        output_text.insert(
            tk.END,
            "-" * 65 + "\n"
        )

        # ---------------- VERIFICATION ----------------
        if user1_shared_secret == user2_shared_secret:
            output_text.insert(
                tk.END,
                "STATUS: SUCCESS\n\n"
            )

            output_text.insert(
                tk.END,
                "Both users generated the same shared secret key.\n"
            )
            output_text.insert(
                tk.END,
                "The Diffie-Hellman key exchange was successful.\n"
            )
            messagebox.showinfo(
                "Success",
                "Diffie-Hellman Key Exchange Successful!\n\n"
                f"Shared Secret Key: {user1_shared_secret}"
            )
        else:
            output_text.insert(
                tk.END,
                "STATUS: FAILED\n\n"
            )
            output_text.insert(
                tk.END,
                "The shared keys are different.\n"
            )
            output_text.insert(
                tk.END,
                "The Diffie-Hellman key exchange failed.\n"
            )
            messagebox.showerror(
                "Failed",
                "Diffie-Hellman Key Exchange Failed!"
            )
    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid integer values."
        )

# ---------------- CLEAR FUNCTION ----------------
def clear_all():
    p_entry.delete(
        0,
        tk.END
    )
    g_entry.delete(
        0,
        tk.END
    )
    user1_private_entry.delete(
        0,
        tk.END
    )
    user2_private_entry.delete(
        0,
        tk.END
    )
    output_text.delete(
        "1.0",
        tk.END
    )

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title(
    "Cybersecurity Practical 5 - Diffie-Hellman Key Exchange"
)
root.geometry(
    "900x750"
)
root.resizable(
    True,
    True
)

# ---------------- TITLE ----------------
title_label = tk.Label(
    root,
    text="DIFFIE-HELLMAN KEY EXCHANGE",
    font=("Arial", 20, "bold")
)
title_label.pack(
    pady=10
)
subtitle_label = tk.Label(
    root,
    text="Cybersecurity Practical 5",
    font=("Arial", 12)
)
subtitle_label.pack(
    pady=2
)

# ---------------- INPUT FRAME ----------------
input_frame = tk.LabelFrame(
    root,
    text="User Input",
    font=("Arial", 12, "bold"),
    padx=15,
    pady=15
)
input_frame.pack(
    fill="x",
    padx=25,
    pady=15
)

# p
tk.Label(
    input_frame,
    text="Prime Number (p):",
    font=("Arial", 11)
).grid(
    row=0,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)
p_entry = tk.Entry(
    input_frame,
    width=25,
    font=("Arial", 11)
)
p_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=8
)
# g
tk.Label(
    input_frame,
    text="Generator (g):",
    font=("Arial", 11)
).grid(
    row=1,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)
g_entry = tk.Entry(
    input_frame,
    width=25,
    font=("Arial", 11)
)
g_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=8
)

# User 1 Private Key
tk.Label(
    input_frame,
    text="User 1 Private Key:",
    font=("Arial", 11)
).grid(
    row=2,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)
user1_private_entry = tk.Entry(
    input_frame,
    width=25,
    font=("Arial", 11)
)
user1_private_entry.grid(
    row=2,
    column=1,
    padx=10,
    pady=8
)

# User 2 Private Key
tk.Label(
    input_frame,
    text="User 2 Private Key:",
    font=("Arial", 11)
).grid(
    row=3,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)
user2_private_entry = tk.Entry(
    input_frame,
    width=25,
    font=("Arial", 11)
)
user2_private_entry.grid(
    row=3,
    column=1,
    padx=10,
    pady=8
)


# ---------------- BUTTONS ----------------
button_frame = tk.Frame(
    root
)
button_frame.pack(
    pady=5
)
calculate_button = tk.Button(
    button_frame,
    text="Calculate Key Exchange",
    command=calculate_keys,
    width=25,
    font=("Arial", 11, "bold")
)
calculate_button.pack(
    side="left",
    padx=10
)
clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_all,
    width=15,
    font=("Arial", 11)
)
clear_button.pack(
    side="left",
    padx=10
)
exit_button = tk.Button(
    button_frame,
    text="Exit",
    command=root.destroy,
    width=15,
    font=("Arial", 11)
)
exit_button.pack(
    side="left",
    padx=10
)


# ---------------- OUTPUT FRAME ----------------
output_frame = tk.LabelFrame(
    root,
    text="Output",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=10
)
output_frame.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=15
)
output_text = tk.Text(
    output_frame,
    height=25,
    width=100,
    font=("Consolas", 10)
)
output_text.pack(
    fill="both",
    expand=True
)

# ---------------- START GUI ----------------
root.mainloop()
