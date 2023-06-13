from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    app.logger.debug('Processing default request')
    if request.method == 'POST': # This checks if the user has made the request via the web page 'index.html'
        city = request.form['city'] # Pulls out the city information input by the user & adds to the url for the api request
        units = request.form['units'] # This adds the unit information selected by the user via the dropdown on the web page & adds to the url for the api request
        weather_data = get_weather(city, units)
        temperature = get_temperature(weather_data)
        wind_speed = get_wind_speed(weather_data)
        return render_template('index.html', temperature=temperature, wind_speed=wind_speed, city=city)
    else:
        return render_template('index.html')

def main(): # The main function will start the flask server
    app.run(debug=True)

def get_weather(city: str, units: str = 'metric'): # Note that metric is selected by default if ever the user did not select a unit of measurement
    with open('openweatherapi.txt', 'r') as file: # Calling the open weather api key text file
        API_KEY = file.read().strip() # Reads the API key from the file
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}'
    response = requests.get(url)
    return response.json()

def get_temperature(weather_data: dict):
    return weather_data['main']['temp']

def get_wind_speed(weather_data: dict):
    return weather_data['wind']['speed'] 

if __name__ == '__main__':
    main()