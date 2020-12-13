weatherApp.py

An application that prompts the user for a city or zip code and requests a
weather report or forecast - based upon the user's selection - from OpenWeatherMap.

weatherApp retrieves the requested city data from OWM, pulls in reverse-geolocation state and county/province
information using the reverse_geocoder module, and then presents the data to the user in an easy-to-read format.
