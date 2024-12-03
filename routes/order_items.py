from flask import Blueprint
from models.order_items import Order_items
from app import db

order_items_bp = Blueprint('order_items', __name__)

@order_items_bp.route('/order_items', methods=['GET'])
def get_order_items():
    # Perform the query on the Order Items model
    t = db.session.query(Order_items).with_entities(
        Order_items.order_id,
        Order_items.order_item_id,
        Order_items.product_id,
        Order_items.seller_id,
        Order_items.shipping_limit_date,
        Order_items.price,
        Order_items.freight_value
    )
    
    # Prepare the response
    ls = []
    for v in t:
        te = {
            "order_id": v.order_id,
            "order_item_id": v.order_item_id,
            "product_id": v.product_id,
            "seller_id": v.seller_id,
            "shipping_limit_date": v.shipping_limit_date,
            "price": v.price,
            "freight_value": v.freight_value
        }
        ls.append(te)
    
    return ls
