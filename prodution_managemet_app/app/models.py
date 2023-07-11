from app import db
from datetime import datetime
from flask_login import UserMixin
from app import login_manager


class Order(db.Model):
    date = db.Column(db.DateTimeField(auto_now_add=True))
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(50), unique=True)
    customer_name = db.Column(db.String(100))
    quantity_ordered = db.Column(db.Integer)
    livred = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Order {self.order_number}>"

class Inventory(db.Model):
    date = db.Column(db.DateTimeField(auto_now_add=True))
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    quantity_in_stock = db.Column(db.Integer)
    quantity_in_input = db.Column(db.Integer)

    def __repr__(self):
        return f"<Inventory {self.product_name}>"

class Schedule(db.Model):
    date_created = db.Column(db.DateTimeField(auto_now_add=True))
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    def __repr__(self):
        return f"<Schedule {self.product_name}>"

class Quality(db.Model):
    date = db.Column(db.DateTimeField(auto_now_add=True))
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    quality_status = db.Column(db.String(20))
    quality_issue = db.Column(db.String(50))

    def __repr__(self):
        return f"<Quality {self.product_name}>"
    
class User(UserMixin, db.Model):
    #User creation method
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))

    def __repr__(self):
        return f"<User {self.username}>"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
