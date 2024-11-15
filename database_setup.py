import sqlite3

# Створення або підключення до бази даних
conn = sqlite3.connect('menu.db')
cursor = conn.cursor()

# Створення таблиці menu_items, якщо її ще не існує
cursor.execute('''
CREATE TABLE IF NOT EXISTS menu_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
)
''')

conn.commit()
conn.close()
