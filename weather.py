import requests
import pandas as pd
import boto3
import mysql.connector

# Define the Open_metreo API endpoint 
open_meteo_api_url = "https://archive-api.open-meteo.com/v1/era5" 

# London coordinates
capetown_latitude = -33.918861
capetown_longitude = 18.423300

# Date range
start_date = "2022-12-21"
end_date = "2023-03-20"

# Define the bucket name
s3_bucket_name = "weather-forecast-data-4-london-capetown"

# Define the CSV file name 
folder_name = "."
csv_file_name = f"{folder_name}/capetown_historical_dec_2022_march_2023.csv"
aws_access_key_id="AKIASBCUUCPA4OCXDNPD"
aws_secret_access_key= "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"
headers = {
    'X-ApiKeys': f'accessKey={aws_access_key_id}; secretKey={aws_secret_access_key}'
}

# MySQL connection parameters
rds_host = "weather-data.cnsut4ztamj5.us-east-1.rds.amazonaws.com"
db_name = "weather_forecast_db"
db_user = "dufuna_admin"
db_password = "Data%Analytics101"

try:
    # Make the API request
    response = requests.get(open_meteo_api_url, headers=headers, params={
        "latitude": capetown_latitude,
        "longitude": capetown_longitude,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": "temperature_2m"
    })

    # Check if the API request was successful
    if response.status_code == 200:
        # Call the function and get the JSON data
        data = response.json()
        # Access the temperature data correctly
        temperature_data = data.get("hourly", {})
        # Create a DataFrame
        df_capetown = pd.DataFrame(temperature_data, columns=['time', 'temperature_2m'])
        # Save the data to a CSV file
        df_capetown.to_csv(csv_file_name, index=False)
        # Upload the CSV file to S3
        s3 = boto3.client("s3")
        s3.upload_file(csv_file_name, s3_bucket_name, csv_file_name)
       
        # Read the CSV data into a Pandas DataFrame
        df = pd.read_csv(csv_file_name)

        # Clean up: Remove the local CSV filec
        # import os
        # os.remove(csv_file_name)

        # Database connection
        try:
            conn = mysql.connector.connect(host=rds_host, database=db_name, user=db_user, password=db_password)
            cursor = conn.cursor()

            # Create a table for capetown 
            create_table_query = """
            CREATE TABLE cape_town_historical_dec_2022_march_2023 (
                timestamp DATETIME,
                temperature_2m FLOAT
            );
            """
            cursor.execute(create_table_query)
            conn.commit()

            # Insert data into the table
            insert_data_query = """
            INSERT INTO weather_forecast_db.cape_town_historical_dec_2022_march_2023 (timestamp, temperature_2m)
            VALUES (%s, %s);
            """
            for row in df.itertuples(index=False):
                cursor.execute(insert_data_query, (row.time, row.temperature_2m))
            conn.commit()
        except mysql.connector.Error as db_err:
            print(f"MySQL Error: {db_err}")
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()
    else:
        print(f"API request failed with status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")