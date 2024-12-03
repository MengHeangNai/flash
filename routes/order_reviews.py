from flask import Blueprint
from models.order_reviews import Order_reviews
from app import db

order_reviews_bp = Blueprint('order_reviews', __name__)

@order_reviews_bp.route('/order_reviews', methods=['GET'])
def get_order_reviews():
    # Perform the query on the Order Reviews model
    t = db.session.query(Order_reviews).with_entities(
        Order_reviews.review_id,
        Order_reviews.order_id,
        Order_reviews.review_score,
        Order_reviews.review_comment_title,
        Order_reviews.review_comment_message,
        Order_reviews.review_creation_date,
        Order_reviews.review_answer_timestamp
    )
    
    # Prepare the response
    ls = []
    for v in t:
        te = {
            "review_id": v.review_id,
            "order_id": v.order_id,
            "review_score": v.review_score,
            "review_comment_title": v.review_comment_title,
            "review_comment_message": v.review_comment_message,
            "review_creation_date": v.review_creation_date,
            "review_answer_timestamp": v.review_answer_timestamp
        }
        ls.append(te)
    
    return ls
