from app import db, Pizza

db.create_all()

initial_pizzas = [
    {"name": "Маргарита", "ingredients": "Сир, томатний соус, базилік", "price": 100.00},
    {"name": "Пепероні", "ingredients": "Сир, пепероні, томатний соус", "price": 120.00},
    {"name": "Гавайська", "ingredients": "Курка, ананас, сир, томатний соус", "price": 150.00},
    {"name": "Капрічоза", "ingredients": "Гриби, шинка, сир, томатний соус", "price": 130.00},
]

for pizza_data in initial_pizzas:
    pizza = Pizza(name=pizza_data["name"], ingredients=pizza_data["ingredients"], price=pizza_data["price"])
    db.session.add(pizza)

db.session.commit()
print("База даних заповнена тестовими даними.")
