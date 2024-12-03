from app import db 

class Seller(db.Model):
    __tablename__ = 'sellers'

    seller_id = db.Column(db.String(50), primary_key=True)
    seller_zip_code_prefix = db.Column(db.Integer, nullable=False)
    seller_city = db.Column(db.String(50), nullable=False)
    seller_state = db.Column(db.String(50), nullable=False)
