import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="coffee_sales_db",
    user="peri***",
    password="********"
)
cur = conn.cursor()

queries = {
    'Sales Summary': """
        SELECT store_location, SUM(money) AS total_sales
        FROM coffee_sales
        GROUP BY store_location
        ORDER BY total_sales DESC;
    """,
    'Sales Trends': """
        SELECT date, SUM(money) AS daily_sales
        FROM coffee_sales
        GROUP BY date
        ORDER BY date;
    """,
    'Weather Impact on Sales': """
        SELECT a.date, a.weather, b.total_sales
        FROM weather_data a
        JOIN (SELECT date, SUM(money) AS total_sales FROM coffee_sales GROUP BY date) b
        ON a.date = b.date;
    """,
    'Top Performing Days': """
        SELECT date, SUM(money) AS total_sales
        FROM coffee_sales
        GROUP BY date
        HAVING SUM(money) > (SELECT AVG(total_sales) FROM (SELECT date, SUM(money) AS total_sales FROM coffee_sales GROUP BY date) sub)
        ORDER BY total_sales DESC;
    """,
    'Rolling Weekly Sales': """
        SELECT date,
               SUM(money) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS rolling_weekly_sales
        FROM coffee_sales
        ORDER BY date;
    """
}

# Execute each query and print the results
for name, query in queries.items():
    print(f"\n{name}:\n" + "-"*40)
    cur.execute(query)
    for row in cur.fetchall():
        print(row)

cur.close()
conn.close()
