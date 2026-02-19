import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Форма авторизации")
root.geometry("300x200")
root.resizable(False, False) 

title_label = tk.Label(root, text="Авторизация", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

username_label = tk.Label(input_frame, text="Username:")
username_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

username_entry = tk.Entry(input_frame, width=20)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(input_frame, text="Password:")
password_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

password_entry = tk.Entry(input_frame, show="*", width=20)  
password_entry.grid(row=1, column=1, padx=5, pady=5)

status_label = tk.Label(root, text="", fg="green", font=("Arial", 10, "bold"))
status_label.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

def submit():
    username = username_entry.get()
    password = password_entry.get()

    if username and password:
        status_label.config(text="Выполнен вход")
    else:
        messagebox.showwarning("Предупреждение", "Заполните оба поля!")

def clear():
    username_entry.delete(0, tk.END)  
    password_entry.delete(0, tk.END)  
    status_label.config(text="") 

def close():
    root.destroy()

submit_button = tk.Button(button_frame, text="Submit", command=submit, width=8)
submit_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Clear", command=clear, width=8)
clear_button.grid(row=0, column=1, padx=5)

close_button = tk.Button(button_frame, text="Close", command=close, width=8)
close_button.grid(row=0, column=2, padx=5)

root.mainloop()
