import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def register():
    register_window = tk.Toplevel(root)
    register_window.title("Регистрация")
    register_window.geometry("300x200")

    label_username = tk.Label(register_window, text="Имя пользователя:")
    entry_username = tk.Entry(register_window)

    label_password = tk.Label(register_window, text="Пароль:")
    entry_password = tk.Entry(register_window, show="*")

    label_confirm_password = tk.Label(register_window, text="Подтвердите пароль:")
    entry_confirm_password = tk.Entry(register_window, show="*")

    def do_register():
        username = entry_username.get()
        password = entry_password.get()
        confirm_password = entry_confirm_password.get()

        if password != confirm_password:
            messagebox.showerror("Ошибка", "Пароли не совпадают.")
            return

        try:
            with open('saves.txt', 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            lines = []

        for line in lines:
            stored_username, _ = line.strip().split(':')
            if username == stored_username:
                messagebox.showerror("Ошибка", "Пользователь с таким именем уже существует.")
                return

        new_line = f"{username}:{password}\n"
        lines.append(new_line)

        with open('saves.txt', 'w') as file:
            file.writelines(lines)

        messagebox.showinfo("Успех", "Регистрация успешна!")
        register_window.destroy()

    button_register = tk.Button(register_window, text="Зарегистрироваться", command=do_register)

    label_username.pack()
    entry_username.pack()
    label_password.pack()
    entry_password.pack()
    label_confirm_password.pack()
    entry_confirm_password.pack()
    button_register.pack()

def login():
    username = entry_username.get()
    password = entry_password.get()

    try:
        with open('saves.txt', 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        lines = []

    for line in lines:
        stored_username, stored_password = line.strip().split(':')
        if username == stored_username and password == stored_password:
            messagebox.showinfo("Вход", "Вход выполнен!")
            show_chessboard()
            return

    messagebox.showerror("Ошибка", "Неверное имя пользователя или пароль.")

def show_chessboard():
    root.withdraw()

    board = tk.Tk()
    board.title("Шахматное поле")
    board.geometry("400x400")

    canvas = tk.Canvas(board, width=400, height=400)
    canvas.pack()

    colors = ["white", "black"]
    for i in range(8):
        for j in range(8):
            color = colors[(i + j) % 2]
            canvas.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50, fill=color)

    board.mainloop()

root = tk.Tk()
root.title("Логин")
root.geometry("300x200")

label_username = tk.Label(root, text="Имя пользователя:")
entry_username = tk.Entry(root)

label_password = tk.Label(root, text="Пароль:")
entry_password = tk.Entry(root, show="*")

button_login = tk.Button(root, text="Войти", command=login)
button_register = tk.Button(root, text="Зарегистрироваться", command=register)
label_username.pack()
entry_username.pack()
label_password.pack()
entry_password.pack()
button_login.pack()
button_register.pack()
root.mainloop()
