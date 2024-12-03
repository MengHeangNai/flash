from flask import Blueprint
from models.seller import Seller
from app import db

seller_bp = Blueprint('seller', __name__)

@seller_bp.route('/seller', methods=['GET'])
def get_seller():
    # Perform the query on the Seller model
    t = db.session.query(Seller).with_entities(
        Seller.seller_id,
        Seller.seller_zip_code_prefix,
        Seller.seller_city,
        Seller.seller_state
    )
    
    # Prepare the response
    ls = []
    for v in t:
        te = {
            "seller_id": v.seller_id,
            "seller_zip_code_prefix": v.seller_zip_code_prefix,
            "seller_city": v.seller_city,
            "seller_state": v.seller_state
        }
        ls.append(te)
    
    return ls

