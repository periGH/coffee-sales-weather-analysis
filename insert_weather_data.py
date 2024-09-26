import psycopg2
import json

# Load the weather JSON data
with open('weather_data.json', 'r') as file:
    data = json.load(file)
    weather_data = data['weather_data']  

conn = psycopg2.connect(
    host="localhost",
    database="coffee_sales_db",
    user="peri***",
    password="*******"
)

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS weather_data (
        date DATE,
        location VARCHAR(50),
        weather VARCHAR(50),
        temperature_c INT,
        humidity INT,
        PRIMARY KEY (date, location)
    );
''')
conn.commit()

for item in weather_data:
    cur.execute(
        '''
        INSERT INTO weather_data (date, location, weather, temperature_c, humidity)
        VALUES (%s, %s, %s, %s, %s) ON CONFLICT (date, location) DO NOTHING;
        ''',
        (item['date'], item['location'], item['weather'], item['temperature_C'], item['humidity'])
    )

conn.commit()

cur.close()
conn.close()

print("Weather data inserted successfully.")
