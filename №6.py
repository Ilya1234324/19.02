import tkinter as tk
from tkinter import messagebox

def save_data():
    name = name_entry.get()
    surname = surname_entry.get()
    class_num = class_entry.get()
    group = group_entry.get()

    if not all([name, surname, class_num, group]):
        messagebox.showwarning("Предупреждение", "Заполните все поля!")
        return

    data_line = f"Имя: {name}, Фамилия: {surname}, Класс: {class_num}, Группа: {group}\n"

    with open("students_data.txt", "a", encoding="utf-8") as file:
        file.write(data_line)

    messagebox.showinfo("Успех", "Данные успешно сохранены!")
    clear_fields()

def clear_fields():
    name_entry.delete(0, tk.END)
    surname_entry.delete(0, tk.END)
    class_entry.delete(0, tk.END)
    group_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Ввод данных студента")
root.geometry("400x250")

tk.Label(root, text="Имя:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Фамилия:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
surname_entry = tk.Entry(root, width=30)
surname_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Номер класса:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
class_entry = tk.Entry(root, width=30)
class_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Группа:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
group_entry = tk.Entry(root, width=30)
group_entry.grid(row=3, column=1, padx=10, pady=10)

save_button = tk.Button(root, text="Сохранить", command=save_data)
save_button.grid(row=4, column=0, pady=20, padx=10, sticky="e")

clear_button = tk.Button(root, text="Очистить", command=clear_fields)
clear_button.grid(row=4, column=1, pady=20, padx=10, sticky="w")

root.mainloop()
