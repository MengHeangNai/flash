from app import db

class Products(db.Model):
    __tablename__ = 'products'

    product_id = db.Column(db.String(50), primary_key=True)
    product_category_name = db.Column(db.String(50), nullable=False)
    product_name_lenght = db.Column(db.Integer, nullable=False)
    product_description_lenght = db.Column(db.Integer, nullable=False)
    product_photos_qty = db.Column(db.Integer, nullable=False)
    product_weight_g = db.Column(db.Float, nullable=False)
    product_length_cm = db.Column(db.Float, nullable=False)
    product_height_cm = db.Column(db.Float, nullable=False)
    product_width_cm = db.Column(db.Float, nullable=False)
