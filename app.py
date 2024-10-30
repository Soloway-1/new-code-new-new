from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzeria.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Pizza {self.name}>'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    menu = Pizza.query.all()
    return render_template('menu.html', menu=menu)

@app.route('/add_pizza', methods=['GET', 'POST'])
def add_pizza():
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients']
        price = float(request.form['price'])
        
        new_pizza = Pizza(name=name, ingredients=ingredients, price=price)
        db.session.add(new_pizza)
        db.session.commit()
        
        return redirect(url_for('menu'))
    return render_template('add_pizza.html')

@app.route('/edit_pizza/<int:pizza_id>', methods=['GET', 'POST'])
def edit_pizza(pizza_id):
    pizza = Pizza.query.get_or_404(pizza_id)
    if request.method == 'POST':
        pizza.name = request.form['name']
        pizza.ingredients = request.form['ingredients']
        pizza.price = float(request.form['price'])
        db.session.commit()
        return redirect(url_for('menu'))
    return render_template('edit_pizza.html', pizza=pizza)

@app.route('/delete_pizza/<int:pizza_id>', methods=['POST'])
def delete_pizza(pizza_id):
    pizza = Pizza.query.get_or_404(pizza_id)
    db.session.delete(pizza)
    db.session.commit()
    return redirect(url_for('menu'))

if __name__ == '__main__':
    app.run(port=1234, debug=True)