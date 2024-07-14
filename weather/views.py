from django.shortcuts import render
import requests

OpenMeteoURL = "https://api.open-meteo.com/v1/forecast"


def home(request):
    return render(request, "home.html")


def results(request):
    latitude = request.POST.get("latitude")
    longitude = request.POST.get("longitude")
    city = request.POST.get("city")

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["temperature_2m", "wind_speed_10m", "relative_humidity_2m"],
        "daily": ["sunrise", "sunset"],
    }

    response = requests.get(OpenMeteoURL, params=params).json()

    data = {
        "name": city,
        "latitude": response["latitude"],
        "longitude": response["longitude"],
        "temperature": response["current"]["temperature_2m"],
        "sunrise": response["daily"]["sunrise"][0].split("T")[
            1
        ],  # getting the exact time, the API gives us a jumble of info
        "sunset": response["daily"]["sunset"][0].split("T")[1],
        "humidity": response["current"]["relative_humidity_2m"],
        "wind_speed": response["current"]["wind_speed_10m"],
    }

    return render(request, "results.html", context={"data": data})


def city_list(request):
    location = request.POST.get("location")
    potential_cities = requests.get(
        f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=15&language=en&format=json"
    ).json()["results"]
    return render(
        request, "city_list.html", context={"potential_cities": potential_cities}
    )
