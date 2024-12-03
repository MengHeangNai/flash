import random
import pandas as pd
from datetime import datetime, timedelta
import uuid

# Global list of US cities with corresponding state and ZIP code prefix
us_cities = [
    {"city": "New York", "state": "NY", "zip_prefix": 100},
    {"city": "Los Angeles", "state": "CA", "zip_prefix": 900},
    {"city": "Chicago", "state": "IL", "zip_prefix": 600},
    {"city": "Houston", "state": "TX", "zip_prefix": 770},
    {"city": "Phoenix", "state": "AZ", "zip_prefix": 850},
    {"city": "Philadelphia", "state": "PA", "zip_prefix": 190},
    {"city": "San Antonio", "state": "TX", "zip_prefix": 782},
    {"city": "San Diego", "state": "CA", "zip_prefix": 921},
    {"city": "Dallas", "state": "TX", "zip_prefix": 752},
    {"city": "San Jose", "state": "CA", "zip_prefix": 951}
]

def generate_uuid():
    return str(uuid.uuid4())

def generate_random_string(length):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))

def generate_customer_data(num_records):
    customers = []
    for _ in range(num_records):
        customer_id = generate_uuid()
        customer_unique_id = generate_uuid()
        city_info = random.choice(us_cities)
        customer_zip_code_prefix = city_info["zip_prefix"] * 100 + random.randint(0, 99)
        customer_city = city_info["city"]
        customer_state = city_info["state"]
        customers.append((customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state))
    return customers

def generate_geolocation_data(num_records):
    geolocations = []
    for _ in range(num_records):
        geolocation_zip_code_prefix = random.randint(10000, 99999)
        geolocation_lat = round(random.uniform(-90, 90), 6)
        geolocation_lng = round(random.uniform(-180, 180), 6)
        city_info = random.choice(us_cities)
        geolocation_city = city_info["city"]
        geolocation_state = city_info["state"]
        geolocations.append((geolocation_zip_code_prefix, geolocation_lat, geolocation_lng, geolocation_city, geolocation_state))
    return geolocations

def generate_order_data(num_records, customer_ids):
    orders = []
    for _ in range(num_records):
        order_id = generate_uuid()
        customer_id = random.choice(customer_ids)
        order_status = random.choice(['delivered', 'shipped', 'canceled', 'invoiced', 'processing'])
        order_purchase_timestamp = datetime.now() - timedelta(days=random.randint(0, 365))
        order_approved_at = order_purchase_timestamp + timedelta(hours=random.randint(1, 48))
        order_delivered_carrier_date = order_approved_at + timedelta(days=random.randint(1, 7))
        order_delivered_customer_date = order_delivered_carrier_date + timedelta(days=random.randint(1, 7))
        order_estimated_delivery_date = order_purchase_timestamp + timedelta(days=random.randint(1, 30))
        orders.append((order_id, customer_id, order_status, order_purchase_timestamp, order_approved_at, order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date))
    return orders

def generate_order_item_data(num_records, order_ids, product_ids, seller_ids):
    order_items = []
    for _ in range(num_records):
        order_id = random.choice(order_ids)
        order_item_id = random.randint(1, 10)
        product_id = random.choice(product_ids)
        seller_id = random.choice(seller_ids)
        shipping_limit_date = datetime.now() + timedelta(days=random.randint(1, 30))
        price = round(random.uniform(10, 500), 2)
        freight_value = round(random.uniform(5, 50), 2)
        order_items.append((order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, freight_value))
    return order_items

def generate_order_payment_data(num_records, order_ids):
    order_payments = []
    unique_entries = set()
    for _ in range(num_records):
        order_id = random.choice(order_ids)
        payment_sequential = random.randint(1, 10)
        payment_type = random.choice(['credit_card', 'voucher', 'boleto'])
        payment_installments = random.randint(1, 12)
        payment_value = round(random.uniform(10, 500), 2)
        entry = (order_id, payment_sequential)
        if entry in unique_entries:
            continue
        unique_entries.add(entry)
        order_payments.append((order_id, payment_sequential, payment_type, payment_installments, payment_value))
    return order_payments

def generate_order_review_data(num_records, order_ids):
    order_reviews = []
    for _ in range(num_records):
        review_id = generate_uuid()
        order_id = random.choice(order_ids)
        review_score = random.randint(1, 5)
        review_comment_title = generate_random_string(20)
        review_comment_message = generate_random_string(100)
        review_creation_date = datetime.now() - timedelta(days=random.randint(0, 365))
        review_answer_timestamp = review_creation_date + timedelta(days=random.randint(1, 30))
        order_reviews.append((review_id, order_id, review_score, review_comment_title, review_comment_message, review_creation_date, review_answer_timestamp))
    return order_reviews

def generate_product_category_name_translation_data(num_records):
    translations = []
    for _ in range(num_records):
        product_category_name = generate_random_string(20)
        product_category_name_english = generate_random_string(20)
        translations.append((product_category_name, product_category_name_english))
    return translations

def generate_product_data(num_records):
    products = []
    for _ in range(num_records):
        product_id = generate_uuid()
        product_category_name = generate_random_string(45)
        product_name_lenght = random.randint(5, 100)  # Corrected column name
        product_description_lenght = random.randint(20, 500)  # Corrected column name
        product_photos_qty = random.randint(1, 10)
        product_weight_g = random.randint(100, 20000)
        product_length_cm = random.randint(10, 200)
        product_height_cm = random.randint(10, 200)
        product_width_cm = random.randint(10, 200)
        products.append((product_id, product_category_name, product_name_lenght, product_description_lenght, product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm))
    return products

def generate_seller_data(num_records):
    sellers = []
    for _ in range(num_records):
        seller_id = generate_uuid()
        city_info = random.choice(us_cities)
        seller_zip_code_prefix = city_info["zip_prefix"] * 100 + random.randint(0, 99)  # Ensure 5-digit ZIP code
        seller_city = city_info["city"]
        seller_state = city_info["state"]
        sellers.append((seller_id, seller_zip_code_prefix, seller_city, seller_state))
    return sellers

def save_to_csv(data, filename, columns):
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(filename, index=False)

def main():
    num_customers = 1000
    num_geolocations = 1000
    num_orders = 1000
    num_order_items = 1000
    num_order_payments = 1000
    num_order_reviews = 1000
    num_product_categories = 100
    num_products = 1000
    num_sellers = 1000

    customers = generate_customer_data(num_customers)
    save_to_csv(customers, 'customers.csv', ['customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'customer_city', 'customer_state'])

    geolocations = generate_geolocation_data(num_geolocations)
    save_to_csv(geolocations, 'geolocation.csv', ['geolocation_zip_code_prefix', 'geolocation_lat', 'geolocation_lng', 'geolocation_city', 'geolocation_state'])

    customer_ids = [customer[0] for customer in customers]
    orders = generate_order_data(num_orders, customer_ids)
    save_to_csv(orders, 'orders.csv', ['order_id', 'customer_id', 'order_status', 'order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date'])

    order_ids = [order[0] for order in orders]
    product_ids = [generate_uuid() for _ in range(num_products)]
    seller_ids = [generate_uuid() for _ in range(num_sellers)]
    order_items = generate_order_item_data(num_order_items, order_ids, product_ids, seller_ids)
    save_to_csv(order_items, 'order_items.csv', ['order_id', 'order_item_id', 'product_id', 'seller_id', 'shipping_limit_date', 'price', 'freight_value'])

    order_payments = generate_order_payment_data(num_order_payments, order_ids)
    save_to_csv(order_payments, 'order_payments.csv', ['order_id', 'payment_sequential', 'payment_type', 'payment_installments', 'payment_value'])

    order_reviews = generate_order_review_data(num_order_reviews, order_ids)
    save_to_csv(order_reviews, 'order_reviews.csv', ['review_id', 'order_id', 'review_score', 'review_comment_title', 'review_comment_message', 'review_creation_date', 'review_answer_timestamp'])

    product_categories = generate_product_category_name_translation_data(num_product_categories)
    save_to_csv(product_categories, 'product_category_name_translation.csv', ['product_category_name', 'product_category_name_english'])

    products = generate_product_data(num_products)
    save_to_csv(products, 'products.csv', ['product_id', 'product_category_name', 'product_name_lenght', 'product_description_lenght', 'product_photos_qty', 'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm'])

    sellers = generate_seller_data(num_sellers)
    save_to_csv(sellers, 'sellers.csv', ['seller_id', 'seller_zip_code_prefix', 'seller_city', 'seller_state'])

if __name__ == "__main__":
    main()

