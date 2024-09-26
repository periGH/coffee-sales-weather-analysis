# pip install requests
import requests

# https://openweathermap.org/forecast5

# API_KEY = '1c05af4204cd*******************'
# lat = '90'
# long = '180'

# url = api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}


# URL pointing to my local server - json file 
url = "http://localhost:8000/weather_data.json"

# make a request to the local server
response = requests.get(url)

# convert the response to JSON format 
weather_data = response.json()

# analyze the weather data
print(weather_data) 