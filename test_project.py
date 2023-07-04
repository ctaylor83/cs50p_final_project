import project

def test_get_weather_ny():
    weather_data = project.get_weather('New York', 'imperial') # Looking to get the weather for New York in Fahrenheit
    assert 'main' in weather_data # confirm the main weather data is present
    assert 'temp' in weather_data['main'] # confirm that temprature is present
    assert 'wind' in weather_data # confirm that wind data is present
    assert 'speed' in weather_data['wind'] # Confirm wind speed is present

def test_get_weather_ldn():
    weather_data = project.get_weather('London', 'metric') # Looking for the weather in London in Celsius
    assert 'main' in weather_data # confirm the main weather data is present
    assert 'temp' in weather_data['main'] # confirm that temprature is present
    assert 'wind' in weather_data # confirm that wind data is present
    assert 'speed' in weather_data['wind'] # Confirm wind speed is present

def test_get_temperature(): # Test to extract the temprature from weather data 
    weather_data = {'main': {'temp': 10}}
    assert project.get_temperature(weather_data) == 10

def test_get_wind_speed(): # Test to extract wind speed from the weather data
    weather_data = {'wind': {'speed': 5}}
    assert project.get_wind_speed(weather_data) == 5

def test_no_input(): # Testing that an error is returned when not inputing any city name
    weather_data = project.get_weather('', 'metric')
    assert weather_data is not None
    assert weather_data.get('cod') == '400'

def test_invalid_city(): # Testing that an invalid city name returns an error
    weather_data = project.get_weather('InvalidCityName', 'imperial') 
    assert weather_data is not None
    assert weather_data.get('cod') == '404'
