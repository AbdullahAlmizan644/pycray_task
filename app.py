#Import All Module
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Database Username
username="root"
#Database Password
password=""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{username}:{password}@localhost/task'
db = SQLAlchemy(app) 
db.init_app(app)

#Create User And Order Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_name = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

with app.app_context():
    db.create_all()

#Find All User
@app.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['name'] = user.name
        user_data['email'] = user.email
        user_data['created_at'] = user.created_at
        output.append(user_data)
    return jsonify({'users': output})


#Find specific User
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    user_data = {}
    user_data['id'] = user.id
    user_data['name'] = user.name
    user_data['email'] = user.email
    user_data['created_at'] = user.created_at
    return jsonify({'user': user_data})


#Find All Orders
@app.route('/orders', methods=['GET'])
def get_all_orders():
    orders = Order.query.all()
    output = []
    for order in orders:
        order_data = {}
        order_data['id'] = order.id
        order_data['user_id'] = order.user_id
        order_data['product_name'] = order.product_name
        order_data['quantity'] = order.quantity
        order_data['total_price'] = order.total_price
        order_data['created_at'] = order.created_at
        output.append(order_data)
    return jsonify({'orders': output})

#Find specific order
@app.route('/orders/<id>', methods=['GET'])
def get_order(id):
    order = Order.query.get_or_404(id)
    order_data = {}
    order_data['id'] = order.id
    order_data['user_id'] = order.user_id
    order_data['product_name'] = order.product_name
    order_data['quantity'] = order.quantity
    order_data['total_price'] = order.total_price
    order_data['created_at'] = order.created_at
    return jsonify({'order': order_data})


if __name__ == '__main__':
    app.run(debug=True)
