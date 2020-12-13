#
# File: weatherApp.py
# Name: Christopher M. Anderson
# Date: 05/30/2019
# Course: DSC510 Intro to Programming
# Week: 12
# Assignment Number: 12.1

# Program Purpose:
#
# An application that prompts the user for a city or zip code and requests a
# weather report or forecast - based upon the user's selection - from OpenWeatherMap.
#
# weatherApp retrieves the requested city data from OWM, pulls in reverse-geolocation state and county/province
# information using the reverse_geocoder module, and then presents the data to the user in an easy-to-read format.
#

# ----------| MODULES |----------

# Import the modules:

import requests
import json
import time
import reverse_geocoder  # module info at: https://github.com/thampiman/reverse-geocoder
import datetime


# ----------| WELCOME AND HEADER |----------

# Let's welcome the user with a brief introduction

# First we create a few variables that style the heading output:

def heading():
    global headingLine
    headingLine = "*" * 75
    headingTitle = "Welcome to the DSC510 Weather Machine!"

    # Print the program header:

    print(headingLine)
    print("{:^75}".format(headingTitle))
    print(headingLine)
    print("\n")
    print("Get a weather report or forecast for any city or ZIP code you desire!\n")


# ----------| MENU |----------

# Prompt the user to enter a city name or zip code to get a weather report or
# forecast and provide a helpful menu system to drive them through the process:

def menu():

    global menuInput, menuForecastCity, menuForecastZIP, menuReportCity, menuReportZIP

    menuInput = input('''
Please make a choice from the menu items below: 

1 for forecast by city
2 for forecast ZIP Code
3 for report by city
4 for report ZIP Code
\n''')

    # Loop the program based upon the user's selection(s):

    if menuInput == '1':
        menuForecastCity = input("What is the city name? ")
        wf.weatherForecastInput()
    elif menuInput == '2':
        try:
            menuForecastZIP = int(input("What is the ZIP code? "))
            wf.weatherForecastInput()
        except ValueError:
            print("\nYou have not entered a valid ZIP code. Please try again.")
    elif menuInput == '3':
        menuReportCity = input("What is the city name? ")
        wr.weatherReportInput()
    elif menuInput == '4':
        try:
            menuReportZIP = int(input("What is the ZIP code? "))
            wr.weatherReportInput()
        except ValueError:
            print("\nYou have not entered a valid ZIP code. Please try again.")
    else:
        print("You have not made a valid entry.")

    return menuInput


# ----------| WEATHER REPORT |----------

# 1) Make a call to the OpenWeatherMap API
# 2) Get current weather data in return and put it into a JSON dictionary
# 3) Print the current weather information to the screen


class WeatherReport:

    def __init__(self):
        self.apiID = "a42694a8daa8291c88ff863a26c2da62"
        self.units = "imperial"
        self.apiWeather = "https://api.openweathermap.org/data/2.5/weather"

    # A method that gets the user's requested city weather information:

    def weatherReportInput(self):

        global requestWeather, weatherReportTitle, weatherData

        # Define the variables that will pass the user's city and the API key
        # to the OWM weather API and make a get request using that information:

        if menuInput == '3':
            payload = {'q': menuReportCity, 'APPID': self.apiID, 'units': self.units}
            requestWeather = requests.get(self.apiWeather, params=payload)
        elif menuInput == '4':
            payload = {'zip': menuReportZIP, 'APPID': self.apiID, 'units': self.units}
            requestWeather = requests.get(self.apiWeather, params=payload)

        # Ensure the connection was successful and that the user made a valid city
        # or ZIP entry and put the returned data from the API into a JSON dictionary:

        requestStatus = requestWeather.status_code
        if requestStatus == 200:  # This is our check to ensure a successful web connection
            print("\nConnecting to OWM... success!")
            weatherData = json.loads(requestWeather.text)
        else:
            print("\nThe city or ZIP code you entered is not valid, or there was a connection error."
                  "\nPlease try again.")
            menu()

        # Define variables for the different types of weather data we will present
        # and get their values from the JSON dictionary we created:

        wCountry = weatherData['sys']['country']
        wTemp = weatherData['main']['temp']
        wWindSpeed = weatherData['wind']['speed']
        wDescription = weatherData['weather'][0]['description']
        wHumidty = weatherData['main']['humidity']
        wPressure = weatherData['main']['pressure']
        wSunrise = weatherData['sys']['sunrise']
        wSunset = weatherData['sys']['sunset']
        wLatitude = weatherData['coord']['lat']
        wLongitude = weatherData['coord']['lon']

        # Let the user know something is happening before the next step:

        if menuInput == '3':
            print("\nLoading the weather data for", menuReportCity, "...\n")
            weatherReportTitle = "Weather Report for " + menuReportCity.capitalize()
        elif menuInput == '4':
            print("\nLoading the weather data for", menuReportZIP, "...\n")
            weatherReportTitle = "Weather Report for " + str(menuReportZIP)

        # OWM does not display state, county, or country information so let's use another webservice
        # and the reverse_geocoder module to get that data from the latitude and longitude information
        # from OWM's data. Module info here: (https://pypi.org/project/reverse_geocoder/)

        # Lookup reverse geographical information based upon latitude and longitude results from OWM:

        coordinates = (wLatitude, wLongitude)
        geoLookupR = reverse_geocoder.search(coordinates)

        # Define variables for the geographical data we will present
        # and get their values from the JSON dictionary we created:

        weatherCity = geoLookupR[0]['name']
        weatherState = geoLookupR[0]['admin1']
        weatherCounty = geoLookupR[0]['admin2']

        # ----------| PRINT WEATHER REPORT |----------

        # This is the area that presents all of our inputted and gathered data into a nice, readable
        # format for the user:

        # DEBUG

        # Uncomment the lines below to print the weather and geolocation data in the JSON dictionaries
        # when running the program. This will help to verify the right URL is getting accessed and that
        # all of the expected information is retrieved:

        # print(requestWeather.url) # <--- Display the full url that we are accessing:
        # print(json.dumps(weatherData, indent=4, sort_keys=True, separators=(',', ':')))
        # print(json.dumps(geoLookupR, indent=4, sort_keys=True, separators=(',', ':')))

        # Print the weather report:

        print("\n")
        print(headingLine)
        print("{:^75}".format(weatherReportTitle.title()))
        print(headingLine)
        print("\n")
        print("City:", weatherCity)
        print("State:", weatherState)
        print("County:", weatherCounty)
        print("Country:", wCountry)
        print("Conditions:", wDescription.capitalize())
        print("Temp:", round(wTemp), "\u00b0" + "F")
        print("Humidity:", wHumidty, "%")
        print("Pressure:", wPressure, "hpa")
        print("Wind:", wWindSpeed, "mph")
        print("Sunrise:", time.ctime(wSunrise))  # Convert from OWM's Unix time to more human readable
        print("Sunset:", time.ctime(wSunset))  # Convert from OWM's Unix time to more human readable
        print("Latitude:", wLatitude)
        print("Longitude:", wLongitude)
        print("\n")
        print(headingLine)


wr = WeatherReport()

# ----------| WEATHER FORECAST |----------

# 1) Make a call to the OpenWeatherMap API
# 2) Get weather forecast data in return and put it into a JSON dictionary
# 3) Print the current weather forecast information to the screen


class WeatherForecast:

    def __init__(self):
        self.apiID = "a42694a8daa8291c88ff863a26c2da62"
        self.units = "imperial"
        self.apiForecast = "https://api.openweathermap.org/data/2.5/forecast"

    # A method that gets the user's requested city weather forecast information:

    def weatherForecastInput(self):

        global requestForecast, weatherForecastTitle, forecastData

        # Define the variables that will pass the user's city and the API key
        # to the OWM forecast API and make a get request using that information:

        if menuInput == '1':
            payload = {'q': menuForecastCity, 'APPID': self.apiID, 'units': self.units}
            requestForecast = requests.get(self.apiForecast, params=payload)
        elif menuInput == '2':
            payload = {'zip': menuForecastZIP, 'APPID': self.apiID, 'units': self.units}
            requestForecast = requests.get(self.apiForecast, params=payload)

        # Ensure the connection was successful and that the user made a valid city
        # or ZIP entry and put the returned data from the API into a JSON dictionary:

        requestStatus = requestForecast.status_code
        if requestStatus == 200:  # This is our check to ensure a successful web connection
            print("\nConnecting to OWM... success!")
            forecastData = json.loads(requestForecast.text)
        else:
            print("\nThe city or ZIP code you entered is not valid, or there was a connection error."
                  "\nPlease try again.")
            menu()

        # Define variables for the different types of weather data we will present
        # and get their values from the JSON dictionary we created:

        forecastCountry = forecastData['city']['country']

        fcTemp01 = forecastData['list'][4]['main']['temp']
        fcTemp02 = forecastData['list'][12]['main']['temp']
        fcTemp03 = forecastData['list'][20]['main']['temp']
        fcTemp04 = forecastData['list'][28]['main']['temp']
        fcTemp05 = forecastData['list'][36]['main']['temp']

        fcDesc01 = forecastData['list'][4]['weather'][0]['description']
        fcDesc02 = forecastData['list'][12]['weather'][0]['description']
        fcDesc03 = forecastData['list'][20]['weather'][0]['description']
        fcDesc04 = forecastData['list'][28]['weather'][0]['description']
        fcDesc05 = forecastData['list'][36]['weather'][0]['description']

        fcWind01 = forecastData['list'][4]['wind']['speed']
        fcWind02 = forecastData['list'][12]['wind']['speed']
        fcWind03 = forecastData['list'][20]['wind']['speed']
        fcWind04 = forecastData['list'][28]['wind']['speed']
        fcWind05 = forecastData['list'][36]['wind']['speed']

        fcHumidity01 = forecastData['list'][4]['main']['humidity']
        fcHumidity02 = forecastData['list'][12]['main']['humidity']
        fcHumidity03 = forecastData['list'][20]['main']['humidity']
        fcHumidity04 = forecastData['list'][28]['main']['humidity']
        fcHumidity05 = forecastData['list'][36]['main']['humidity']

        # forecastPressure = forecastData['list'][0]['main']['pressure']

        forecastLatitude = forecastData['city']['coord']['lat']
        forecastLongitude = forecastData['city']['coord']['lon']

        # Let the user know something is happening before the next step:

        if menuInput == '1':
            print("\nLoading the weather data for", menuForecastCity, "...\n")
            weatherForecastTitle = "Weather Forecast for " + menuForecastCity.capitalize()
        elif menuInput == '2':
            print("\nLoading the weather data for", menuForecastZIP, "...\n")
            weatherForecastTitle = "Weather Forecast for " + str(menuForecastZIP)

        # OWM does not display state, county, or country information so let's use another webservice
        # and the reverse_geocoder module to get that data from the latitude and longitude information
        # from OWM's data. Module info here: (https://pypi.org/project/reverse_geocoder/)

        # Lookup reverse geographical information based upon latitude and longitude results from OWM:

        coordinates = (forecastLatitude, forecastLongitude)
        geoLookupF = reverse_geocoder.search(coordinates)

        # Define variables for the geographical data we will present
        # and get their values from the JSON dictionary we created:

        forecastCity = geoLookupF[0]['name']
        forecastState = geoLookupF[0]['admin1']
        forecastCounty = geoLookupF[0]['admin2']

        # Define variables for getting the dates in the forecast to display nicely:

        day1 = datetime.date.today() + datetime.timedelta(days=1)
        day2 = datetime.date.today() + datetime.timedelta(days=2)
        day3 = datetime.date.today() + datetime.timedelta(days=3)
        day4 = datetime.date.today() + datetime.timedelta(days=4)
        day5 = datetime.date.today() + datetime.timedelta(days=5)

        # ----------| PRINT WEATHER FORECAST |----------

        # This is the area that presents all of our inputted and gathered data into a nice, readable
        # format for the user:

        # DEBUG

        # Uncomment the lines below to print the weather and geolocation data in the JSON dictionaries
        # when running the program. This will help to verify the right URL is getting accessed and that
        # all of the expected information is retrieved:

        # print(requestForecast.url)  # <--- Display the full url that we are accessing:
        # print(json.dumps(forecastData, indent=4, sort_keys=True, separators=(',', ':')))
        # print(json.dumps(geoLookupF, indent=4, sort_keys=True, separators=(',', ':')))

        # Print the forecast:

        # Print the heading and a few geographic bits of information.

        print("\n")
        print(headingLine)
        print("{:^75}".format(weatherForecastTitle.title()))
        print(headingLine)
        print("\n")
        print("City:", forecastCity)
        print("State:", forecastState)
        print("County:", forecastCounty)
        print("Country:", forecastCountry)
        print("\n")

        # Print the five day forecast:

        print("Five-Day Forecast:")
        print("\n")
        print('{:<14}'.format("Date"), '{:<12}'.format("Temp"), '{:<10}'.format("Wind"), '{:<18}'.format("Humidity"),
              "Outlook")
        print("-" * 75)
        print('{:<14}'.format(day1.strftime("%b %d")), round(fcTemp01), '{:<9}'.format("\u00b0" + "F"),
              round(fcWind01), '{:<11}'.format("mph"), round(fcHumidity01), '{:<9}'.format("%"), str.capitalize(fcDesc01))
        print('{:<14}'.format(day2.strftime("%b %d")), round(fcTemp02), '{:<9}'.format("\u00b0" + "F"),
              round(fcWind02), '{:<11}'.format("mph"), round(fcHumidity02), '{:<9}'.format("%"), str.capitalize(fcDesc02))
        print('{:<14}'.format(day3.strftime("%b %d")), round(fcTemp03), '{:<9}'.format("\u00b0" + "F"),
              round(fcWind03), '{:<11}'.format("mph"), round(fcHumidity03), '{:<9}'.format("%"), str.capitalize(fcDesc03))
        print('{:<14}'.format(day4.strftime("%b %d")), round(fcTemp04), '{:<9}'.format("\u00b0" + "F"),
              round(fcWind04), '{:<11}'.format("mph"), round(fcHumidity04), '{:<9}'.format("%"), str.capitalize(fcDesc04))
        print('{:<14}'.format(day5.strftime("%b %d")), round(fcTemp05), '{:<9}'.format("\u00b0" + "F"),
              round(fcWind05), '{:<11}'.format("mph"), round(fcHumidity05), '{:<9}'.format("%"), str.capitalize(fcDesc05))
        print("\n")
        print(headingLine)


wf = WeatherForecast()


# ----------| REPEAT |----------

# Ask the user if they would like to continue getting more weather information:

def repeat():
    global repeatSelection
    answer = "y"
    while answer == "y":
        repeatSelection = input('''
Would you like to run the program again?

y for Yes
n for No
''')
        if repeatSelection.lower() == "y":
            menu()
            continue
        elif repeatSelection.lower() == "n":
            print("Thanks for using the DSC510 Weather Machine, see you next time!")
            break
        else:
            print("That was not a valid selection. Please try again.")
        continue


# ----------| MAIN |----------

def main():
    if __name__ == '__main__':
        heading()
        menu()
        repeat()


main()
