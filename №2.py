from tkinter import Tk, Label, Entry, Button, messagebox
import re 

root = Tk()
root.title("Авторизация")
root.geometry("300x200")

username_label = Label(root, text="Логин:")
username_label.pack(pady=5)

password_label = Label(root, text="Пароль:")
password_label.pack(pady=5)

username_entry = Entry(root)
username_entry.pack(pady=5)

password_entry = Entry(root, show="*")
password_entry.pack(pady=5)

def login():
    username = username_entry.get()
    password = password_entry.get()

    if len(password) < 8:
        messagebox.showerror("Ошибка", "Пароль должен содержать не менее 8 символов!")
        return

    if not re.search(r'[!@#$%^&*]', password):
        messagebox.showerror("Ошибка", "Пароль должен содержать спецсимволы (!@#$%^&*).")
        return

    if not re.search(r'\d', password):
        messagebox.showerror("Ошибка", "Пароль должен содержать хотя бы одну цифру.")
        return

    if not re.search(r'[A-Z]', password):
        messagebox.showerror("Ошибка", "Пароль должен содержать заглавные буквы.")
        return

    if not re.search(r'[a-z]', password):
        messagebox.showerror("Ошибка", "Пароль должен содержать строчные буквы.")
        return

    if username == "Илья" and password == "Ilya123_@":
        messagebox.showinfo("Успех", "Вы вошли в систему!")
        root.destroy()
        root2.open()
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль!")

login_button = Button(root, text="Войти", command=login)
login_button.pack(pady=20)

root.mainloop()

root2 = Tk()
root2.title("Вошли в систему")
root2.geometry("300x200")
root2.configure(bg="purple")

label_pobeda = Label (root2, text="ТЫ КРАСАУЧИК", bg='purple')
label_pobeda.place(x=105, y=80)

root2.mainloop()


