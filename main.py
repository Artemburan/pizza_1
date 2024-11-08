from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.get("/menu/")
def menu():
    pizzas = [
    {"name":"Маргаріта", "ingredients": "Томатний соус, моцарела, помідори, базилік", "price": 200},
    {"name":"Гавайська", "ingredients": "Консервований ананас, ніжне куряче філе, сири моцарела та пармезан", "price": 240},
    {"name": "4 сира", "ingredients": "Вершковий соус, сир: моцарела, чеддер, твердий, блакитний сир", "price": 220}
    ]
    return render_template("menu.html", pizzas=pizzas)

if __name__ == "__main__":
    app.run(debug=True, port=80)