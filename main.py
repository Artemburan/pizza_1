from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.get("/menu/")
def menu():
    pizzas = [
        {"name": "Маргаріта", "ingredients": "Томатний соус, моцарела, помідори, базилік", "price": 200},
        {"name": "Гавайська", "ingredients": "Консервований ананас, ніжне куряче філе, сири моцарела та пармезан", "price": 240},
        {"name": "4 сира", "ingredients": "Вершковий соус, сир: моцарела, чеддер, твердий, блакитний сир", "price": 220}
    ]
    conn = sqlite3.connect('menu.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM menu_items")
    pizzas = cursor.fetchall()
    conn.close()
    return render_template("menu.html", pizzas=pizzas)

@app.route("/admin/", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        name = request.form["name"]
        description = request.form["description"]
        price = float(request.form["price"])

        conn = sqlite3.connect('menu.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO menu_items (name, description, price) VALUES (?, ?, ?)", (name, description, price))
        conn.commit()
        conn.close()

        return redirect(url_for("menu"))

    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True, port=80)
