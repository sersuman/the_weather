import requests
from django.shortcuts import render


def index(request):
    url = 'https://samples.openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22'
    city = 'Las Vegas'
    
    r = requests.get(url.format(city))
    print(r.text)
    return render(request, 'weather/weather.html')
