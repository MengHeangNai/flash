from flask import Blueprint
from models.order_payments import Order_payments
from app import db

order_payments_bp = Blueprint('order_payments', __name__)

@order_payments_bp.route('/order_payments', methods=['GET'])
def get_order_payments():
    # Perform the query on the Order Payments model
    t = db.session.query(Order_payments).with_entities(
        Order_payments.order_id,
        Order_payments.payment_sequential,
        Order_payments.payment_type,
        Order_payments.payment_installments,
        Order_payments.payment_value
    )
    
    # Prepare the response
    ls = []
    for v in t:
        te = {
            "order_id": v.order_id,
            "payment_sequential": v.payment_sequential,
            "payment_type": v.payment_type,
            "payment_installments": v.payment_installments,
            "payment_value": v.payment_value
        }
        ls.append(te)
    
    return ls
