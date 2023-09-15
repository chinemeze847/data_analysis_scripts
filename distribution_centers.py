import pandas as pd
import mysql.connector
from config.db_config import DB_CONFIG
from mysql.connector import Error

file = './distribution_centers.csv'
df = pd.read_csv(file)

# Replace NaN values with a default value
df.fillna('', inplace=True)

try:
    connection = mysql.connector.connect(
        host=DB_CONFIG['host'],
        database=DB_CONFIG['database'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        connection_timeout=600,
    )
    if connection.is_connected():
        cursor = connection.cursor()
except Error as e:
    print("Error while connecting to MySQL", e)

table_name = 'distribution_centers'
for index, row in df.iterrows():
    insert_query = f'''INSERT INTO {table_name} 
              (id, name, longitude, latitude) 
              VALUES (%s, %s, %s, %s)'''
    values = (row[0], row[1], row[2], row[3])
    try:
        cursor.execute(insert_query, values)
        connection.commit()
    except Error as e:
        print("Error while inserting data into MySQL", e)
if connection.is_connected():
    cursor.close()
    connection.close()