from flask import Blueprint
from models.orders import Orders
from app import db

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['GET'])
def get_orders():
    # Perform the query on the Orders model
    t = db.session.query(Orders).with_entities(
        Orders.order_id,
        Orders.customer_id,
        Orders.order_status,
        Orders.order_purchase_timestamp,
        Orders.order_approved_at,
        Orders.order_delivered_carrier_date,
        Orders.order_delivered_customer_date,
        Orders.order_estimated_delivery_date
    )
    
    # Prepare the response
    ls = []
    for v in t:
        te = {
            "order_id": v.order_id,
            "customer_id": v.customer_id,
            "order_status": v.order_status,
            "order_purchase_timestamp": v.order_purchase_timestamp,
            "order_approved_at": v.order_approved_at,
            "order_delivered_carrier_date": v.order_delivered_carrier_date,
            "order_delivered_customer_date": v.order_delivered_customer_date,
            "order_estimated_delivery_date": v.order_estimated_delivery_date
        }
        ls.append(te)
    
    return ls
