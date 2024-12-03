from app import db

class Order_payments(db.Model):
    __tablename__ = 'order_payments'

    order_id = db.Column(db.String(50), primary_key=True)
    payment_sequential = db.Column(db.Integer, primary_key=True)
    payment_type = db.Column(db.String(50), nullable=False)
    payment_installments = db.Column(db.Integer, nullable=False)
    payment_value = db.Column(db.Float, nullable=False)
