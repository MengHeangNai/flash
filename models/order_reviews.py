from app import db

class Order_reviews(db.Model):
    __tablename__ = 'order_reviews'

    review_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(50), nullable=False)
    review_score = db.Column(db.Integer, nullable=False)
    review_comment_title = db.Column(db.String(50), nullable=False)
    review_comment_message = db.Column(db.String(50), nullable=False)
    review_creation_date = db.Column(db.DateTime, nullable=False)
    review_answer_timestamp = db.Column(db.DateTime, nullable=False)