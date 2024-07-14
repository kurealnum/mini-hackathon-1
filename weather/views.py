from django.shortcuts import render
import requests


def home(request):
    return render(request, "home.html")


def results(request):
    latitude = request.POST.get("latitude")
    longitude = request.POST.get("longitude")

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ["temperature_2m"],
    }

    response = requests.get(OpenMeteoURL, params=params).json()

    data = {
        "latitude": response["latitude"],
        "longitude": response["longitude"],
        "temperature": response["current"]["temperature_2m"],
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
