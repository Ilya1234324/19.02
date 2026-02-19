import tkinter as tk
from tkinter import messagebox

def show_position(position_name):
    messagebox.showinfo("Позиция", f"Кнопка расположена: {position_name}")

root = tk.Tk()
root.title("Кнопки по диагонали")
root.geometry("430x330")

btn_nw = tk.Button(root, text="1", command=lambda: show_position("в верхнем левом углу"))
btn_nw.place(x=10, y=10)

btn_ne = tk.Button(root, text="2", command=lambda: show_position("в верхнем правом углу"))
btn_ne.place(x=390, y=10)

btn_sw = tk.Button(root, text="3", command=lambda: show_position("в нижнем левом углу"))
btn_sw.place(x=10, y=290)

btn_se = tk.Button(root, text="4", command=lambda: show_position("в нижнем правом углу"))
btn_se.place(x=390, y=290)

root.mainloop()