from flask import Blueprint
from models.products import Products

from app import db

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['GET'])
def get_products():
    # Perform the query on the Products model
    t = db.session.query(Products).with_entities(
        Products.product_id,
        Products.product_category_name,
        Products.product_name_lenght,
        Products.product_description_lenght,
        Products.product_photos_qty,
        Products.product_weight_g,
        Products.product_length_cm,
        Products.product_height_cm,
        Products.product_width_cm
    )
    
    # Prepare the response
    ls = []
    for v in t:
        te = {
            "product_id": v.product_id,
            "product_category_name": v.product_category_name,
            "product_name_lenght": v.product_name_lenght,
            "product_description_lenght": v.product_description_lenght,
            "product_photos_qty": v.product_photos_qty,
            "product_weight_g": v.product_weight_g,
            "product_length_cm": v.product_length_cm,
            "product_height_cm": v.product_height_cm,
            "product_width_cm": v.product_width_cm
        }
        ls.append(te)
    
    return ls

@products_bp.route('/products/<string:product_id>', methods=['GET'])
def get_product(product_id):
    # Perform the query on the Products model
    t = db.session.query(Products).with_entities(
        Products.product_id,
        Products.product_category_name,
        Products.product_name_lenght,
        Products.product_description_lenght,
        Products.product_photos_qty,
        Products.product_weight_g,
        Products.product_length_cm,
        Products.product_height_cm,
        Products.product_width_cm
    ).filter(Products.product_id == product_id).first()
    
    # Prepare the response
    te = {
        "product_id": t.product_id,
        "product_category_name": t.product_category_name,
        "product_name_lenght": t.product_name_lenght,
        "product_description_lenght": t.product_description_lenght,
        "product_photos_qty": t.product_photos_qty,
        "product_weight_g": t.product_weight_g,
        "product_length_cm": t.product_length_cm,
        "product_height_cm": t.product_height_cm,
        "product_width_cm": t.product_width_cm
    }
    
    return te

@products_bp.route('/products/<string:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # Perform the query on the Products model
    t = db.session.query(Products).filter(Products.product_id == product_id).first()
    
    # Delete the product
    db.session.delete(t)
    db.session.commit()
    
    return "Product deleted successfully"

@products_bp.route('/products', methods=['POST'])
def add_product():
    # Get the request data
    data = request.get_json()
    
    # Create a new Products object
    new_product = Products(
        product_id = data['product_id'],
        product_category_name = data['product_category_name'],
        product_name_lenght = data['product_name_lenght'],
        product_description_lenght = data['product_description_lenght'],
        product_photos_qty = data['product_photos_qty'],
        product_weight_g = data['product_weight_g'],
        product_length_cm = data['product_length_cm'],
        product_height_cm = data['product_height_cm'],
        product_width_cm = data['product_width_cm']
    )
    
    # Add the new product to the database
    db.session.add(new_product)
    db.session.commit()
    
    return "Product added successfully"

@products_bp.route('/products/<string:product_id>', methods=['PUT'])
def update_product(product_id):
    # Get the request data
    data = request.get_json()
    
    # Perform the query on the Products model
    t = db.session.query(Products).filter(Products.product_id == product_id).first()
    
    # Update the product
    t.product_category_name = data['product_category_name']
    t.product_name_lenght = data['product_name_lenght']
    t.product_description_lenght = data['product_description_lenght']
    t.product_photos_qty = data['product_photos_qty']
    t.product_weight_g = data['product_weight_g']
    t.product_length_cm = data['product_length_cm']
    t.product_height_cm = data['product_height_cm']
    t.product_width_cm = data['product_width_cm']
    
    db.session.commit()
    
    return "Product updated successfully"