from app import db

class Product_category_name_translation(db.Model):
    __tablename__ = 'product_category_name_translation'

    product_category_name = db.Column(db.String(50), primary_key=True)
    product_category_name_english = db.Column(db.String(50), nullable=False)