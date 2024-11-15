import sqlite3

conn = sqlite3.connect('menu.db')
cursor = conn.cursor()

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
