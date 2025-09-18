import tkinter as tk
from tkinter import messagebox, PhotoImage
import pyodbc


def connect_to_db():
    try:
        DB_CONFIG = {
            'server': r'412-04\MSSQLSERVER2024',
            'database': 'App',
            'trusted_connection': 'yes',
            'driver': '{ODBC Driver 17 for SQL Server}'
        }
        CONNECTION_STRING = f"""
        DRIVER={DB_CONFIG['driver']};
        SERVER={DB_CONFIG['server']};
        DATABASE={DB_CONFIG['database']};
        Trusted_Connection={DB_CONFIG['trusted_connection']};
        """

        conn = pyodbc.connect(CONNECTION_STRING)

        # Выполнение запроса
        cursor = conn.cursor()
        cursor.execute("SELECT Name FROM Users")
        rows = cursor.fetchall()

        for row in rows:
            username = row[0].strip()
            output_text.insert(tk.END, username + '\n')

        # Закрытие соединения
        cursor.close()
        conn.close()

    except Exception as e:
        messagebox.showerror("Ошибка", str(e))


root = tk.Tk()
root.title("Подключение к SQL Server")
icon = PhotoImage(file="5165c0bc7395b99eab49329784ab7ff5.png")
root.iconphoto(False, icon)

img = PhotoImage(file='5165c0bc7395b99eab49329784ab7ff5.png')

# Кнопка для подключения
btn_connect = tk.Button(
    root, text="Подключиться и получить пользователей", command=connect_to_db)
btn_connect.pack(pady=10)

# Текстовое поле для отображения результатов
output_text = tk.Text(root, width=50, height=15)
output_text.pack(pady=10)

img_label = tk.Label(root, image=img)
img_label.pack(pady=10)


# Запуск главного цикла приложения
root.mainloop()
