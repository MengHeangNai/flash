from app import db

class Customers(db.Model):
    __tablename__ = "customers"

    customer_id = db.Column(db.Integer, primary_key=True)
    customer_unique_id = db.Column(db.String(50), nullable=False)
    customer_zip_code_prefix = db.Column(db.Integer, nullable=False)
    customer_city = db.Column(db.String(50), nullable=False)
    customer_state = db.Column(db.String(50), nullable=False)
