from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    app.logger.debug('Processing default request')
    if request.method == 'POST': # This checks if the user has made the request via the web page 'index.html'
        city = request.form['city'] # Pulls out the city information input by the user & adds to the url for the api request
        units = request.form['units'] # This adds the unit information selected by the user via the dropdown on the web page & adds to the url for the api request
        weather_data = get_weather(city, units)

        if weather_data is None:  # Check if there's an error message in the response
            flash('City not found, please try again') # Warn the user that they have selected an incorrect city
            return redirect(url_for('index'))  # Redirect back to index page
        
        else:
            temperature = get_temperature(weather_data)
            wind_speed = get_wind_speed(weather_data)
            weather_description, weather_icon = get_weather_info(weather_data)
            return render_template('index.html', temperature=temperature, wind_speed=wind_speed, city=city, weather_description=weather_description, weather_icon=weather_icon)
    else:
        return render_template('index.html')

def main(): # The main function will start the flask server
    app.run(debug=True)

def get_weather(city: str, units: str = 'metric'): # Note that metric is selected by default if ever the user did not select a unit of measurement
    with open('openweatherapi.txt', 'r') as file: # Calling the open weather api key text file
        API_KEY = file.read().strip() # Reads the API key from the file
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}'
    response = requests.get(url)
    data = response.json()
    return data

def get_temperature(weather_data: dict): # extracts the weather info from the weather data dictionary
    return weather_data['main']['temp']

def get_wind_speed(weather_data: dict): # extracts the wind speed data from the weather data dictionary
    return weather_data['wind']['speed'] 

def get_weather_info(weather_data: dict):
    return weather_data['weather'][0]['description'], weather_data['weather'][0]['icon']


if __name__ == '__main__':
    app.secret_key = 'cs50pyweather' # Secret key set to enable Flask flash function
    main()