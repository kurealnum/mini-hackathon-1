from django.shortcuts import render
import openmeteo_requests
from openmeteo_sdk.Variable import Variable
import requests

OpenMeteoClient = openmeteo_requests.Client()
OpenMeteoURL = "https://api.open-meteo.com/v1/forecast"


def home(request):
    return render(request, "home.html")


def results(request):
    latitude = request.POST.get("latitude")
    longitude = request.POST.get("longitude")
    location = request.POST.get("location")

    # if the user entered a location instead of lat and long
    if location:
        response = requests.get(
            f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1&language=en&format=json"
        )
        latitude_and_longitude = response.json()["results"][0]
        latitude = latitude_and_longitude["latitude"]
        longitude = latitude_and_longitude["longitude"]

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["temperature_2m"],
    }

    response = OpenMeteoClient.weather_api(
        "https://api.open-meteo.com/v1/forecast", params=params
    )[0]
    # the current weather data
    current = response.Current()

    # this is all from here: https://github.com/open-meteo/python-requests/blob/main/README.md
    current_variables = list(
        map(lambda i: current.Variables(i), range(0, current.VariablesLength()))  # type: ignore
    )

    current_temperature_2m = next(
        filter(
            lambda x: x.Variable() == Variable.temperature,  # type: ignore
            current_variables,
        )
    )

    data = {
        "latitude": response.Latitude(),
        "longitude": response.Longitude(),
        "temperature": current_temperature_2m.Value(),  # type: ignore
    }

    return render(request, "results.html", context={"data": data})
