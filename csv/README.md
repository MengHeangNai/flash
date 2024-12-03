```markdown
# Database Design and Modeling with PostgreSQL and MySQL

This repository contains sample data and scripts for the book "Database Design and Modeling with PostgreSQL and MySQL". Below are the instructions to generate sample data and load it into the database using provided Python scripts.

## Directory Structure

.
├── MySQL                         # Directory containing MySQL scripts
├── config.ini                    # Configuration file for database connection
├── customers.csv                 # Sample data file for customers
├── generate_shop_spehere_data.py # Script to generate sample data
├── load_csv_mysql.py             # Script to load CSV data into MySQL database
├── order_items.csv               # Sample data file for order items
├── orders.csv                    # Sample data file for orders
├── products.csv                  # Sample data file for products
└── sellers.csv                   # Sample data file for sellers


## Prerequisites

- Python 3.x
- MySQL server
- Required Python libraries (install via `pip`)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/Database-Design-and-Modeling-with-PostgreSQL-and-MySQL.git
    cd Database-Design-and-Modeling-with-PostgreSQL-and-MySQL/ch03
    ```

2. **Install the required Python libraries**:
    ```bash
    pip install -r requirements.txt
    ```

    Ensure your `requirements.txt` includes the necessary libraries:
    ```
    mysql-connector-python
    pandas
    configparser
    ```

3. **Configure database connection**:
    Edit the `config.ini` file with your MySQL database connection details:
    ```ini
    [mysql]
    host = localhost
    user = your_username
    password = your_password
    database = your_database
    ```

## Generating Sample Data

To generate sample data, use the `generate_shop_spehere_data.py` script:
```bash
python generate_shop_spehere_data.py
```

This script will generate sample data and store it in the respective CSV files.

## Loading Data into MySQL

1. **Load data using `load_csv_mysql.py`**:
    ```bash
    python load_csv_mysql.py
    ```

    This script reads the CSV files and loads the data into the specified MySQL database tables.

## CSV Files

- `customers.csv`: Contains customer data.
- `order_items.csv`: Contains order item data.
- `orders.csv`: Contains order data.
- `products.csv`: Contains product data.
- `sellers.csv`: Contains seller data.
- `geolocation.csv`: Contains geolocaton data
- `order_payments.csv`: Contains order payments data
- `product_category_name_translation.csv`: Contains product category data
- `order_reviews.csv`: Contains order reviews data

## Additional Information

Ensure that the MySQL database and tables are set up correctly before running the scripts. You can find SQL scripts to create the necessary tables in the `MySQL` directory.

## Contact

For any questions or issues, please contact `alkin.tezuysal@gmail.com`.
```

This `README.md` provides a clear and comprehensive guide for users to understand the project structure, prerequisites, and the steps to generate and load sample data into the database.
