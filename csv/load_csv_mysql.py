import mysql.connector
import pandas as pd
import configparser

def get_db_connection():
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    try:
        connection = mysql.connector.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            database=config['mysql']['database']
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def get_column_names(connection, table_name):
    cursor = connection.cursor()
    cursor.execute(f"DESCRIBE {table_name}")
    columns = cursor.fetchall()
    column_names = [column[0] for column in columns]
    cursor.close()
    return column_names

def format_sql_value(value):
    if pd.isna(value):
        return 'NULL'
    return "'{}'".format(str(value).replace("'", "''"))

def truncate_table(connection, table_name):
    cursor = connection.cursor()
    try:
        cursor.execute(f"TRUNCATE TABLE {table_name}")
        connection.commit()
    except Exception as e:
        print(f"Error truncating table {table_name}: {e}")
    finally:
        cursor.close()

def load_csv_to_mysql(connection, table_name, csv_file_path, has_headers=True):
    cursor = connection.cursor()
    try:
        df = pd.read_csv(csv_file_path, header=0 if has_headers else None)
        column_names = get_column_names(connection, table_name)
        print(f"CSV Columns: {df.columns.tolist()}")
        print(f"Table Columns: {column_names}")

        if not has_headers:
            if len(df.columns) != len(column_names):
                raise ValueError(f"Length mismatch: Expected {len(column_names)} columns, but CSV file has {len(df.columns)} columns.")
            df.columns = column_names

        for index, row in df.iterrows():
            values = [format_sql_value(row[col]) for col in column_names]
            placeholders = ', '.join(values)
            sql = "INSERT INTO {} ({}) VALUES ({})".format(table_name, ', '.join(column_names), placeholders)
            cursor.execute(sql)

        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

if __name__ == "__main__":
    connection = get_db_connection()
    if connection is None:
        print("Failed to connect to the database. Please check your credentials and try again.")
        exit(1)

    table_files = {
        'customers': 'customers.csv',
        'geolocation': 'geolocation.csv',
        'orders': 'orders.csv',
        'order_items': 'order_items.csv',
        'order_payments': 'order_payments.csv',
        'order_reviews': 'order_reviews.csv',
        'product_category_name_translation': 'product_category_name_translation.csv',
        'products': 'products.csv',
        'sellers': 'sellers.csv'
    }

    for table_name in table_files.keys():
        print(f"Truncating table {table_name}...")
        truncate_table(connection, table_name)

    for table_name, csv_file_path in table_files.items():
        print(f"Loading data into {table_name} from {csv_file_path}...")
        load_csv_to_mysql(connection, table_name, csv_file_path)

    if connection:
        connection.close()

