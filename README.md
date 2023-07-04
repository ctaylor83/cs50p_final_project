    # WeatherPy
    #### Video Demo:  https://www.youtube.com/watch?v=uTcCcI9wn7k
    #### Description: A simple web based app using Python and Flask.

    On running the project.py file, a local server is run that the user can open via holding down Ctrl & Clicking on the link.

    On doing so a browser page opens and takes the user to a simple web page.  Here the user is asked for input:
    * Input the city that they wish to know the weather for
    * Select from the dropdown the temprature in either Celcius or Farenheit

    Once done the user clicks on "Get Weather".  This will make an api call to OpenWeatherMap to retrieve the city and temprature information.   This information is then returned to the user, providing the current weather, temprature and wind speed.

    There are a few files that make up this program:
    * project.py - This is the main file for the project, located in the root directory.  This is used to run the program.
    * test_project.py - Pytest file with tests written to test out various functinos within the project file.
    * requirements.txt - This lists out the Python packages that is required in order to run this projext
    *openweatherapi.txt - This contains the api key for OpenWeatherMap.  project.py calls on this file to extract the api key as part of the url when requesting the weather for the user's specified location.
    * templates/index.html - This contains the basic html file for the web page that the user views.  This is contained in the templates folder for Flask to access.
    * static/styles.css - This contains the basic css styles sheet that is used alongside index.html to add a little colour to the page!

    Several design choices were considered, including adding in icons for the weather.  I debated not doing this as I wished to focus on Python and keep HTML/CSS fairly basic, however I liked the idea of some basic weather icons to display for the user.  I then found out that I can pull through these images from OpenWeatherMap itself.

    In addition I like the option of adding in multiple cities or saving the previous search almost like creating a weather dashboard, however I am using the free api for OpenWeatherMap so was concerned that this may cause me to use up all of my tokens!

    I had done some research into both Flask and Django for this project.  As I was looking to make a simple application it seemed that Flask was probably the better of the two as Flack seemed to be the better application for small lightweight web apps, and was overall simplere to learn and use.

