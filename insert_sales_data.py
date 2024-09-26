import psycopg2
import pandas as pd

# Load the CSV data
sales_data = pd.read_csv('coffee_sales_dataset.csv')

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",  # the database host
    database="coffee_sales_db",  # the database name
    user="peri****",  # PostgreSQL username
    password="********"  # PostgreSQL password
)

# Create a cursor object
cur = conn.cursor()

# Create table -if not exists
cur.execute('''
    CREATE TABLE IF NOT EXISTS coffee_sales (
        id SERIAL PRIMARY KEY,
        date DATE,
        datetime TIMESTAMP,
        cash_type VARCHAR(10),
        card VARCHAR(50),
        money DECIMAL,
        coffee_name VARCHAR(50),
        customer_id VARCHAR(50),
        store_location VARCHAR(50),
        customer_age INT,
        customer_gender VARCHAR(10),
        loyalty_program BOOLEAN,
        discount DECIMAL
    );
''')
conn.commit()

for i, row in sales_data.iterrows():
    cur.execute(
        '''
        INSERT INTO coffee_sales (date, datetime, cash_type, card, money, coffee_name, customer_id, store_location, customer_age, customer_gender, loyalty_program, discount)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        ''',
        tuple(row)
    )

# # Commit the changes
# conn.commit()

# # Check the number of entries
# cur.execute('SELECT COUNT(*) FROM coffee_sales;')
# count = cur.fetchone()
# print(f"Total rows inserted: {count[0]}")

# # Retrieve and print a sample of data
# cur.execute('SELECT * FROM coffee_sales LIMIT 5;')
# sample_data = cur.fetchall()
# for record in sample_data:
#     print(record)

# Close the connection
cur.close()
conn.close()

