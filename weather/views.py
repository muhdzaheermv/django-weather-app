import requests
from django.shortcuts import render

def index(request):
    weather_data = None
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'bdd9e3b54e2a9e1c9e7cc2a29cc610ce'  # Replace with your OpenWeatherMap API key
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url).json()

        if response.get('cod') == 200:
            weather_data = {
                'city': city.title(),
                'temp': response['main']['temp'],
                'description': response['weather'][0]['description'].title(),
                'country': response['sys']['country'],
                'humidity': response['main']['humidity'],
                'wind_speed': response['wind']['speed'],
    }
        else:
            weather_data = {'city': city.title(), 'temp': 'N/A', 'description': 'City not found', 'country': ''}

    return render(request, 'weather/index.html', {'weather': weather_data})
