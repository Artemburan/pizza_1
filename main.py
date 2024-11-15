from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Головна сторінка
@app.route("/")
def index():
    return render_template("index.html")

# Сторінка з меню
@app.get("/menu/")
def menu():
    conn = sqlite3.connect('menu.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menu_items")
    pizzas = cursor.fetchall()
    conn.close()
    return render_template("menu.html", pizzas=pizzas)

# Сторінка для адміністратора
@app.route("/admin/", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        price = float(request.form["price"])

        # Додавання страви в базу даних
        conn = sqlite3.connect('menu.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO menu_items (name, description, price) VALUES (?, ?, ?)", (name, description, price))
        conn.commit()
        conn.close()

        return redirect(url_for("menu"))

    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True, port=80)
