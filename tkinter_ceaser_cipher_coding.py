import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) + start)
        else:
            result += char
    return result

def encrypt_message(event=None):
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        encrypted = caesar_cipher(text, shift)
        result_text.delete(0, tk.END)
        result_text.insert(0, encrypted)
    except ValueError:
        result_text.delete(0, tk.END)
        result_text.insert(0, "Shift must be an integer!")

def quit_program(event=None):
    if messagebox.askokcancel("Quit", "Do you want to exit the program?"):
        window.destroy()

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher")
window.geometry("400x250")

# Message input
tk.Label(window, text="Enter your message:").pack()
entry_text = tk.Entry(window, width=40)
entry_text.pack()

# Shift input
frame_shift = tk.Frame(window)
frame_shift.pack()

label_shift = tk.Label(frame_shift, text="Enter the shift (e.g., 3):")
label_shift.grid(row=0, column=0, padx=5, pady=5)

entry_shift = tk.Entry(frame_shift, width=5)
entry_shift.grid(row=0, column=1, padx=5, pady=5)

# Encrypt button
button_encrypt = tk.Button(window, text="Encrypt", command=encrypt_message)
button_encrypt.pack(pady=5)
button_encrypt.bind('<Return>', lambda event: encrypt_message())  # Enter key support

# Result field
tk.Label(window, text="Encrypted message:").pack()
result_text = tk.Entry(window, width=40)
result_text.pack()

# End button
button_end = tk.Button(window, text="End (or press Esc)", command=quit_program)
button_end.pack(pady=10)
button_end.bind('<Return>', lambda event: quit_program())  # Enter key support

# Key bindings
window.bind('<Return>', encrypt_message)  # Enter in text fields triggers encryption
window.bind('<KP_Enter>', encrypt_message)  # Numpad Enter
window.bind('<Escape>', quit_program)  # Escape key quits

# Set focus to message entry on start
entry_text.focus_set()

window.mainloop()