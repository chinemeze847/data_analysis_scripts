import pandas as pd
import mysql.connector
from config.db_config import DB_CONFIG
from mysql.connector import Error

file = './users.csv'
df = pd.read_csv(file)

# Replace NaN values with a default value
df.fillna('', inplace=True)

try:
    connection = mysql.connector.connect(
        host=DB_CONFIG['host'],
        database=DB_CONFIG['database'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password']
    )
    if connection.is_connected():
        cursor = connection.cursor()
except Error as e:
    print("Error while connecting to MySQL", e)

table_name = 'users'
insert_query = f'''INSERT INTO {table_name} 
          (id, first_name, last_name, email, age, gender, state, street_address, postal_code, city, country,
          latitude, longitude, traffic_source, created_at) VALUES 
          (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

# Convert DataFrame to list of tuples
data_to_insert = df.to_records(index=False).tolist()

try:
    cursor.executemany(insert_query, data_to_insert)
    connection.commit()
except Error as e:
    print("Error while inserting data into MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()