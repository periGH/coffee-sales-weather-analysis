# coffee-sales-weather-analysis

This project explores the impact of weather conditions on coffee sales using SQL practices. The analysis integrates weather data with sales records to understand trends and the influence of different weather types on sales performance.

## Table of Contents
- [Project Structure](#project-structure)
- [Visualizations](#visualizations)
- [Usage](#usage)
- [Goal](#goal)
- [Required Libraries and Installation](#required-libraries-and-installation)
- [Setup Instructions](#setup-instructions)
- [PostgreSQL Commands](#postgresql-commands)

## Project Structure
- `coffee_sales_dataset.csv`: The main dataset containing historical sales data of coffee.
- `weather_data.json`: Weather data that includes daily weather conditions.
- `queries.sql`: SQL queries used for extracting and analyzing sales data.
- `insert_sales_data.py`: Script for inserting sales data into a PostgreSQL database.
- `insert_weather_data.py`: Script for inserting weather data into the database.
- `combine_sales_weather_data.py`: Python script to combine sales and weather data for analysis.
- `execute_queries.py`: Script to execute SQL queries and analyze data.
- `sales_analysis_visualization.py`: Python script for visualizing sales data.
- `sales_analysis_visualization.ipynb`: Jupyter notebook for interactive data visualization.

## Visualizations
This project includes various visualizations to depict sales trends, the impact of weather on sales, and more, helping to draw meaningful insights from the data.

## Usage
To replicate the analysis:
1. Set up a PostgreSQL database and update the connection settings in the Python scripts.
2. Run the Python scripts to insert data into the database.
3. Execute the SQL queries to perform the analysis.
4. View the Jupyter notebook for detailed visualizations.

## Goal
The goal of this repository is to demonstrate SQL practices in data handling and analysis, applicable to business scenarios.

Feel free to explore the repository and use the methodologies for similar analyses!

## Required Libraries and Installation
This project requires these Python libraries below for database interaction and visualizationas: 

- **psycopg2**: For PostgreSQL database connectivity.
    $ pip install psycopg2
- **pandas**: For data manipulation and analysis 
    $ pip install pandas
- **matplotlib**: For visualization
    $ pip install matplotlib

## Setup Instructions
### Setting up PostgreSQL locally (on Mac):
1. Install PostgreSQL: $ brew install postgresql (bash) 
2. Start PostgreSQL Service: $ brew services start postgresql
3. Create a Database: 
    - access postgresql: $ psql postgres
    - create the database: $ CREATE DATABASE coffee_sales_db;
4. Create a Table for Sales Data:
    - connect to the database: $ \c coffee_sales_db;
    - create the table: 

    CREATE TABLE coffee_sales (
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
5. Insert Data by executing the script: $ python insert_sales_data.py
6. Indexing(create indexes on the columns): 

    CREATE INDEX idx_store_location ON coffee_sales(store_location);
    CREATE INDEX idx_date ON coffee_sales(date);

7. Check if the indexes were created successfully and to see existing indexes on a table: 

    SELECT indexname, indexdef
    FROM pg_indexes
    WHERE tablename = 'coffee_sales';


### PostgreSQL Commands
#### User and Role Management
- `\du`  
  *List all users and roles.*

- `ALTER USER 'user_name' WITH PASSWORD 'new_password';`  
  *Reset the password for a user.*

#### Database and Session Management
- `psql -U postgres`  
  *Connect to PostgreSQL using the `postgres` user (bash command).*

- `\l` or `\list`  
  *List all available databases.*

- `\q`  
  *Exit the PostgreSQL session.*

#### Running SQL Files
- `\i queries.sql`  
  *Run the SQL commands from a file.*

#### Table Management
- `\dt`  
  *List all tables in the current database.*

#### Dropping a Database
1. `\c postgres`  
   *Connect to the `postgres` database or another database of your choice.*
2. `DROP DATABASE coffee_sales_db;`  
   *Drop the `coffee_sales_db` database.*

