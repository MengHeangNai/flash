from app import db 

class Order_items(db.Model):
    __tablename__ = 'order_items'

    order_id = db.Column(db.String(50), primary_key=True)
    order_item_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(50), nullable=False)
    seller_id = db.Column(db.String(50), nullable=False)
    shipping_limit_date = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)
    freight_value = db.Column(db.Float, nullable=False)