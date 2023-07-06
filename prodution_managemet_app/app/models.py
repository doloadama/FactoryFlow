from app import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_number = db.Column(db.String(50), unique=True)
    # Define other fields for the Order model
    
    def __repr__(self):
        return f"<Order {self.order_number}>"
