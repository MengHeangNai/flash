from flask import Blueprint
from models.customers import Customers
from app import db

customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/customers', methods=['GET'])
def get_customers():
    t = db.session.query(Customers).with_entities(
        Customers.customer_id,
        Customers.customer_unique_id,
        Customers.customer_zip_code_prefix,
        Customers.customer_city,
        Customers.customer_state
    )
    
    ls = []
    for v in t:
        te = {
            "id": v.customer_id,
            "unique_id": v.customer_unique_id,
            "zip_code_prefix": v.customer_zip_code_prefix,
            "city": v.customer_city,
            "state": v.customer_state
        }
        ls.append(te)
    
    return ls