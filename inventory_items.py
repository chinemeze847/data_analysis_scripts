import pandas as pd
import mysql.connector
from config.db_config import DB_CONFIG
from mysql.connector import Error


def insert_batch_data(data, cursor, insert_query):
    batch_size = 1000  
    total_rows = len(data)
    for i in range(0, total_rows, batch_size):
        batch_data = data[i:i + batch_size]
        cursor.executemany(insert_query, batch_data)
        cursor.execute("COMMIT")


file = './inventory_items.csv'  
batch_size = 1000  

df = pd.read_csv(file)

# Replace NaN values with a default value
df.fillna('', inplace=True)

try:
    connection = mysql.connector.connect(
         host=DB_CONFIG['host'],
        database=DB_CONFIG['database'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        connect_timeout=600,  
        connection_timeout=600
    )
    if connection.is_connected():
        cursor = connection.cursor()
except Error as e:
    print("Error while connecting to MySQL", e)

table_name = 'inventory_items'

# Convert DataFrame to a list of tuples
data_to_insert = df.to_records(index=False).tolist()

insert_query = f'''INSERT INTO {table_name} 
        (id, product_id, created_at, sold_at, cost, product_category, product_name,
        product_brand, product_retail_price, product_department, product_sku, product_distribution_center_id) 
        VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s,%s, %s, %s)'''

try:
    insert_batch_data(data_to_insert, cursor, insert_query)
except Error as e:
    print("Error while inserting data into MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
