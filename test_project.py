import project

def test_get_weather_ny():
    weather_data = project.get_weather('New York', 'imperial') # Looking to get the weather for New York in Fahrenheit
    assert 'main' in weather_data
    assert 'temp' in weather_data['main']
    assert 'wind' in weather_data
    assert 'speed' in weather_data['wind']

def test_get_weather_ldn():
    weather_data = project.get_weather('London', 'metric') # Looking for the weather in London in Celsius
    assert 'main' in weather_data
    assert 'temp' in weather_data['main']
    assert 'wind' in weather_data
    assert 'speed' in weather_data['wind']

def test_get_temperature():
    weather_data = {'main': {'temp': 10}}
    assert project.get_temperature(weather_data) == 10

def test_get_wind_speed():
    weather_data = {'wind': {'speed': 5}}
    assert project.get_wind_speed(weather_data) == 5

def test_get_weather_info():
    weather_data = {
        'weather': [
            {'description': 'light rain', 'icon': '10d'}
        ],
    }
    assert get_weather_info(weather_data) == ('light rain', '10d')