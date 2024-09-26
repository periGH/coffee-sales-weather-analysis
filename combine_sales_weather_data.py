import pandas as pd
import json
import matplotlib.pyplot as plt

sales_data = pd.read_csv('coffee_sales_dataset.csv')

with open('weather_data.json') as f: 
    weather_json = json.load(f)

# Convert the list of weather data into a dictionary
weather_data = {(item['date'], item['location']): item['weather'] for item in weather_json['weather_data']}

# Add weather data to sales data
# Create a new column for weather in the sales data
def get_weather(row):
    date = row['date']
    location = row['Store_Location']
    return weather_data.get((date, location), 'Unknown')

# Apply the function to each row
sales_data['Weather'] = sales_data.apply(get_weather, axis=1)

# Analyze the Effect of Weather on Sales:
weather_sales_analysis = sales_data.groupby('Weather')['money'].mean()
print(weather_sales_analysis)
weather_sales_analysis.to_csv('weather_sales_analysis.csv')

weather_sales_analysis.plot(kind='bar')
plt.title('Average Coffee Sales by Weather')
plt.ylabel('Average Sales (money)')
plt.savefig('weather_sales_analysis.png') 
plt.show() 
