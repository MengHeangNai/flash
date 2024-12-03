from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root2003@127.0.0.1:3306/shopsphere'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# log connection to the database
print("Connecting to database...")

# Initialize the database
from models.customers import Customers
from models.geolocation import Geolocation
from models.order_items import Order_items
from models.order_payments import Order_payments
from models.order_reviews import Order_reviews
from models.orders import Orders
from models.product_category_name_translation import Product_category_name_translation
from models.products import Products
from models.seller import Seller


db.init_app(app)
# Create the database tables

with app.app_context():
    db.create_all()

# Import and register blueprints
from routes import (
    customers_bp,
    geolocation_bp,
    order_items_bp,
    order_payments_bp,
    order_reviews_bp,
    orders_bp,
    product_category_name_translation_bp,
    products_bp,
    seller_bp
)

app.register_blueprint(customers_bp, url_prefix='/api/v1')
app.register_blueprint(geolocation_bp, url_prefix='/api/v1')
app.register_blueprint(order_items_bp, url_prefix='/api/v1')
app.register_blueprint(order_payments_bp, url_prefix='/api/v1')
app.register_blueprint(order_reviews_bp, url_prefix='/api/v1')
app.register_blueprint(orders_bp, url_prefix='/api/v1')
app.register_blueprint(product_category_name_translation_bp, url_prefix='/api/v1')
app.register_blueprint(products_bp, url_prefix='/api/v1')
app.register_blueprint(seller_bp, url_prefix='/api/v1')

# Define a Blueprint for API versioning

@api_v1.route('/', methods=['GET'])
def default():
    return {"msg": "Welcome to ShopSphere API"}

# @api_v1.route('/customers', methods=['GET'])
# def get_customers():
#     # Perform the query on the Customers model
#     t = db.session.query(Customers).with_entities(
#         Customers.customer_id,
#         Customers.customer_unique_id,
#         Customers.customer_zip_code_prefix,
#         Customers.customer_city,
#         Customers.customer_state
#     )
    
#     # Prepare the response
#     ls = []
#     for v in t:
#         te = {
#             "id": v.customer_id,
#             "unique_id": v.customer_unique_id,
#             "zip_code_prefix": v.customer_zip_code_prefix,
#             "city": v.customer_city,
#             "state": v.customer_state
#         }
#         ls.append(te)
    
#     return ls

# @api_v1.route('/geolocation', methods=['GET'])
# def get_geolocation():
#     # Perform the query on the Geolocation model
#     t = db.session.query(Geolocation).with_entities(
#         Geolocation.geolocation_zip_code_prefix,
#         Geolocation.geolocation_lat,
#         Geolocation.geolocation_lng,
#         Geolocation.geolocation_city,
#         Geolocation.geolocation_state
#     )
    
#     # Prepare the response
#     ls = []
#     for v in t:
#         te = {
#             "zip_code_prefix": v.geolocation_zip_code_prefix,
#             "lat": v.geolocation_lat,
#             "lng": v.geolocation_lng,
#             "city": v.geolocation_city,
#             "state": v.geolocation_state
#         }
#         ls.append(te)
    
#     return ls

# @api_v1.route('/order_items', methods=['GET'])
# def get_order_items():
#     # Perform the query on the Order Items model
#     t = db.session.query(Order_items).with_entities(
#         Order_items.order_id,
#         Order_items.order_item_id,
#         Order_items.product_id,
#         Order_items.seller_id,
#         Order_items.shipping_limit_date,
#         Order_items.price,
#         Order_items.freight_value
#     )
    
#     # Prepare the response
#     ls = []
#     for v in t:
#         te = {
#             "order_id": v.order_id,
#             "order_item_id": v.order_item_id,
#             "product_id": v.product_id,
#             "seller_id": v.seller_id,
#             "shipping_limit_date": v.shipping_limit_date,
#             "price": v.price,
#             "freight_value": v.freight_value
#         }
#         ls.append(te)
    
#     return ls

# @api_v1.route('/order_payments', methods=['GET'])
# def get_order_payments():
#     # Perform the query on the Order Payments model
#     t = db.session.query(Order_payments).with_entities(
#         Order_payments.order_id,
#         Order_payments.payment_sequential,
#         Order_payments.payment_type,
#         Order_payments.payment_installments,
#         Order_payments.payment_value
#     )
    
#     # Prepare the response
#     ls = []
#     for v in t:
#         te = {
#             "order_id": v.order_id,
#             "payment_sequential": v.payment_sequential,
#             "payment_type": v.payment_type,
#             "payment_installments": v.payment_installments,
#             "payment_value": v.payment_value
#         }
#         ls.append(te)
    
#     return ls

# @api_v1.route('/order_reviews', methods=['GET'])
# def get_order_reviews():
#     # Perform the query on the Order Reviews model
#     t = db.session.query(Order_reviews).with_entities(
#         Order_reviews.review_id,
#         Order_reviews.order_id,
#         Order_reviews.review_score,
#         Order_reviews.review_comment_title,
#         Order_reviews.review_comment_message,
#         Order_reviews.review_creation_date,
#         Order_reviews.review_answer_timestamp
#     )
    
#     # Prepare the response
#     ls = []
#     for v in t:
#         te = {
#             "review_id": v.review_id,
#             "order_id": v.order_id,
#             "review_score": v.review_score,
#             "review_comment_title": v.review_comment_title,
#             "review_comment_message": v.review_comment_message,
#             "review_creation_date": v.review_creation_date,
#             "review_answer_timestamp": v.review_answer_timestamp
#         }
#         ls.append(te)
    
#     return ls

# @api_v1.route('/orders', methods=['GET'])
# def get_orders():
#     # Perform the query on the Orders model
#     t = db.session.query(Orders).with_entities(
#         Orders.order_id,
#         Orders.customer_id,
#         Orders.order_status,
#         Orders.order_purchase_timestamp,
#         Orders.order_approved_at,
#         Orders.order_delivered_carrier_date,
#         Orders.order_delivered_customer_date,
#         Orders.order_estimated_delivery_date
#     )
    
#     # Prepare the response
#     ls = []
#     for v in t:
#         te = {
#             "order_id": v.order_id,
#             "customer_id": v.customer_id,
#             "order_status": v.order_status,
#             "order_purchase_timestamp": v.order_purchase_timestamp,
#             "order_approved_at": v.order_approved_at,
#             "order_delivered_carrier_date": v.order_delivered_carrier_date,
#             "order_delivered_customer_date": v.order_delivered_customer_date,
#             "order_estimated_delivery_date": v.order_estimated_delivery_date
#         }
#         ls.append(te)
    
#     return ls

# @api_v1.route('/product_category_name_translation', methods=['GET'])
# def get_product_category_name_translation():
#     # Perform the query on the Product Category Name Translation model
#     t = db.session.query(Product_category_name_translation).with_entities(
#         Product_category_name_translation.product_category_name,
#         Product_category_name_translation.product_category_name_english
#     )
    
#     # Prepare the response
#     ls = []
#     for v in t:
#         te = {
#             "product_category_name": v.product_category_name,
#             "product_category_name_english": v.product_category_name_english
#         }
#         ls.append(te)
    
#     return ls

# @api_v1.route('/products', methods=['GET'])
# def get_products():
#     # Perform the query on the Products model
#     t = db.session.query(Products).with_entities(
#         Products.product_id,
#         Products.product_category_name,
#         Products.product_name_lenght,
#         Products.product_description_lenght,
#         Products.product_photos_qty,
#         Products.product_weight_g,
#         Products.product_length_cm,
#         Products.product_height_cm,
#         Products.product_width_cm
#     )
    
#     # Prepare the response
#     ls = []
#     for v in t:
#         te = {
#             "product_id": v.product_id,
#             "product_category_name": v.product_category_name,
#             "product_name_lenght": v.product_name_lenght,
#             "product_description_lenght": v.product_description_lenght,
#             "product_photos_qty": v.product_photos_qty,
#             "product_weight_g": v.product_weight_g,
#             "product_length_cm": v.product_length_cm,
#             "product_height_cm": v.product_height_cm,
#             "product_width_cm": v.product_width_cm
#         }
#         ls.append(te)
    
#     return ls

# @api_v1.route('/seller', methods=['GET'])
# def get_seller():
#     # Perform the query on the Seller model
#     t = db.session.query(Seller).with_entities(
#         Seller.seller_id,
#         Seller.seller_zip_code_prefix,
#         Seller.seller_city,
#         Seller.seller_state
#     )
    
#     # Prepare the response
#     ls = []
#     for v in t:
#         te = {
#             "seller_id": v.seller_id,
#             "seller_zip_code_prefix": v.seller_zip_code_prefix,
#             "seller_city": v.seller_city,
#             "seller_state": v.seller_state
#         }
#         ls.append(te)
    
#     return ls


# Register the Blueprint with the app
app.register_blueprint(api_v1)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
