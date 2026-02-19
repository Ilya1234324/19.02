import tkinter as tk
from tkinter import messagebox
import csv

root = tk.Tk()
root.title("№3")
root.geometry("400x200")

CSV_FILE_PATH = "passwords.csv"

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=10)

def calculate_hash(password):
    return sum(ord(char) for char in password)

def hash_password():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Предупреждение", "Пожалуйста, введите пароль!")
        return
    hash_value = calculate_hash(password)
    result_label.config(text=f"Хеш-сумма: {hash_value}")

def save_to_csv(password, hash_value):
    with open(CSV_FILE_PATH, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([password, hash_value])

def save_password():
    password = password_entry.get()
    hash_value = calculate_hash(password)
    if not password:
        messagebox.showwarning("Предупреждение", "Пожалуйста, введите пароль!")
        return
    save_to_csv(password, hash_value)
    messagebox.showinfo("Успех", "Пароль и хеш-сумма сохранены в файле!")

def clear_csv():
    with open(CSV_FILE_PATH, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Пароль", "Хеш-сумма"]) 
    messagebox.showinfo("Успех", "CSV-файл очищен!")

result_label = tk.Label(root, text="Хеш-сумма: ")
result_label.pack(pady=5)

hash_button = tk.Button(root, text="Hash", command=hash_password)
hash_button.place(x=80,y=100)

save_button = tk.Button(root, text="Сохранить", command=save_password)
save_button.place(x=165,y=100)

clear_button = tk.Button(root, text="Очистить", command=clear_csv)
clear_button.place(x=275,y=100)

root.mainloop()
