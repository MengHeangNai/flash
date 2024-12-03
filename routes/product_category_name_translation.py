from flask import Blueprint
from models.product_category_name_translation import Product_category_name_translation
from app import db

product_category_name_translation_bp = Blueprint('product_category_name_translation', __name__)

@product_category_name_translation_bp.route('/product_category_name_translation', methods=['GET'])
def get_product_category_name_translation():
    # Perform the query on the Product Category Name Translation model
    t = db.session.query(Product_category_name_translation).with_entities(
        Product_category_name_translation.product_category_name,
        Product_category_name_translation.product_category_name_english
    )
    
    # Prepare the response
    ls = []
    for v in t:
        te = {
            "product_category_name": v.product_category_name,
            "product_category_name_english": v.product_category_name_english
        }
        ls.append(te)
    
    return ls
