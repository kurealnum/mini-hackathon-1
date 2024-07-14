from django.urls import path
from .views import home, results, city_list

urlpatterns = [
    path("home/", home, name="home"),
    path("results/", results, name="results"),
    path("city_list/", city_list, name="city_list"),
]
