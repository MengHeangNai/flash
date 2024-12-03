from app import db

class Orders(db.Model):
    __tablename__ = 'orders'

    order_id = db.Column(db.String(50), primary_key=True)
    customer_id = db.Column(db.String(50), nullable=False)
    order_status = db.Column(db.String(50), nullable=False)
    order_purchase_timestamp = db.Column(db.DateTime, nullable=False)
    order_approved_at = db.Column(db.DateTime, nullable=False)
    order_delivered_carrier_date = db.Column(db.DateTime, nullable=False)
    order_delivered_customer_date = db.Column(db.DateTime, nullable=False)
    order_estimated_delivery_date = db.Column(db.DateTime, nullable=False)