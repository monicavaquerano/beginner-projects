"""
👉 Day 92 Challenge
Today's challenge is to create your own weather app.

👉 To start you off, we've found a free weather API, so here's the starter code for that. All you need to do is customize your timezone, longitude and latitude. This code gets the max & min temperature and weather code.

'''
import requests, json
timezone = "GMT"
latitude = 51.5002
longitude = -0.1262
result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")
user = result.json()
print(json.dumps(user, indent=2))
'''

Your weather app should:
1. Get the weather for your local area.
2. Output the forecast for today. It should show (in a really nice way):
    i. The text version of what the weather code means.
    ii. Max & min temperatures.

Hints:
* Get the longitude & latitude for your nearest city.
* Smash out a massive if ... elif...else selection statement.
* Use Boolean operators (and, or, not) to check for more than one weather code in the same elif, eg: elif code==1 or code==2 or code==3:
"""

import requests, json

# 48.800334742633346, 9.808518608969315
timezone = "CET"
latitude = 48.80
longitude = 9.82

result = requests.get(
    f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}"
)

# Checks for the response
if result.status_code != 200:
    print("An error in the API has ocurred. Try later.")
    exit()

# Object
user = result.json()
# print(json.dumps(user, indent=2))

# Variables
weatherCode = user["daily"]["weathercode"][0]
maxTemp = user["daily"]["temperature_2m_max"][0]
minTemp = user["daily"]["temperature_2m_min"][0]


# Parse weather codes
def getCode(code):
    if code == 0:
        return "Clear sky ☀️"
    elif 1 <= code <= 3:
        return "Mainly clear, partly cloudy, and overcast 🌤️"
    elif code == 45 or code == 48:
        return "Fog and depositing rime fog 🌫️"
    elif code == 51 or code == 53 or code == 55:
        return "Drizzle: Light , moderate and dense intensity 🌧️"
    elif 56 <= code <= 57:
        return "Frizzing Drizzle: Light abd dense intensity 🌧️ 🌨️"
    elif code == 61 or code == 63 or code == 65:
        return "Rain: Slight, moderate and heavy intensity ☔ 🌧️"
    elif code == 66 or code == 67:
        return "Freezing Rain: Light and heavy intensity 🌧️ 🌨️ ❄️"
    elif code == 71 or code == 73 or code == 75:
        return "Snow fall: Slight, moderate and heavy intensity 🌨️ ❄️"
    elif code == 77:
        return "Snow grains 🌨️ ❄️ ☃️"
    elif 80 <= code <= 82:
        return "Rain showers: Slight, moderate and violent ☔ 🌧️ 🌀"
    elif 85 <= code <= 86:
        return "Snow showers: Slight and heavy ☂️ 🌨️ ☃️"
    elif code == 95:
        return "Thunderstorm: Slight or moderate 🌩️ ⛈️"
    elif code == 96 or code == 98:
        return "Thunderstorm with slight and heavy hail 🌩️ 🌨️ ⛈️ ❄️"
    else:
        return "Unknown weather code ❓"


# Print today's weather
title = f"{'Weather Report':=^60}"
weatherReport = f"Today's weather will be:\n{getCode(weatherCode)}\nMax 🔥 : {maxTemp} C° 🥵\tMin ❄️  : {minTemp} C° 🥶"

print(title)
print(weatherReport)
print(f"{'':=^60}")
