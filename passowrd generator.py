import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length < 1:
        password_label.config(text="Invalid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text="Generated Password: " + password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("361x381+500+200")

# Create and pack widgets
length_label = tk.Label(window, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(window)
length_entry.pack()

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(window, text="")
password_label.pack()

# Start the main loop
window.mainloop()
