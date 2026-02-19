import tkinter as tk
from tkinter import messagebox

def analyze_data():
    input_text = entry.get()

    if not input_text:
        messagebox.showwarning("Предупреждение", "Поле ввода пустое!")
        return

    items = [item.strip() for item in input_text.split(',')]

    items_with_digits = []

    for item in items:
        if any(char.isdigit() for char in item):
            items_with_digits.append(item)

    total_items = len(items)
    items_with_numbers_count = len(items_with_digits)
    items_without_numbers_count = total_items - items_with_numbers_count
    
    result_text = (
        f"Всего элементов: {total_items}\n"
        f"Элементов с цифрами (0-9): {items_with_numbers_count}\n"
        f"Элементов без цифр: {items_without_numbers_count}"
    )

    result_label.config(text=result_text)

    if items_with_digits:
        detailed_list = "\n".join(f"  • {item}" for item in items_with_digits)
        detailed_result = f"Элементы с цифрами:\n{detailed_list}"
        detailed_label.config(text=detailed_result)
    else:
        detailed_label.config(text="Элементы с цифрами не найдены")

def clear_fields():
    """Очищает поле ввода и результаты"""
    entry.delete(0, tk.END)
    result_label.config(text="Результаты появятся здесь")
    detailed_label.config(text="Детализация появится здесь")

root = tk.Tk()
root.title("Анализ данных на наличие цифр")
root.geometry("500x500")
root.resizable(False, False)

instruction_label = tk.Label(
    root,
    text="Введите данные через запятую:",
    font=("Arial", 10)
)

instruction_label.pack(pady=10)

entry = tk.Entry(root, width=50, font=("Arial", 10))
entry.pack(pady=5)

analyze_button = tk.Button(
    root,
    text="Анализировать",
    command=analyze_data,
    bg="lightblue",
    font=("Arial", 10)
)

analyze_button.pack(pady=10)

clear_button = tk.Button(
    root,
    text="Очистить",
    command=clear_fields,
    bg="lightcoral",
    font=("Arial", 10)
)

clear_button.pack(pady=5)

result_label = tk.Label(
    root,
    text="Результаты появятся здесь",
    font=("Arial", 10),
    justify="left",
    anchor="w"
)

result_label.pack(pady=10, padx=20, anchor="w")

detailed_label = tk.Label(
    root,
    text="Детализация появится здесь",
    font=("Arial", 9),
    justify="left",
    anchor="w",
    fg="darkgreen"
)

detailed_label.pack(pady=5, padx=20, anchor="w")

root.mainloop()
