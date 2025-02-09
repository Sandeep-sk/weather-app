from django.shortcuts import render
import requests 
import datetime
def home(request):
    city = request.POST.get('city', 'mohali')
    if not city:
        city = 'mohali'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=972e2c41d9666b571cff6f580122bf5d'
    data = requests.get(url).json()
    data=requests.get(url).json()
    payload = {
        'name': data.get('name', 'N/A'),
        'weather': data['weather'][0]['main'] if 'weather' in data and len(data['weather']) > 0 else 'N/A',
        'description': data['weather'][0]['description'] if 'weather' in data and len(data['weather']) > 0 else 'N/A',
        'country': data['sys']['country'] if 'sys' in data and 'country' in data['sys'] else 'N/A',
        'icon': data['weather'][0]['icon'] if 'weather' in data and len(data['weather']) > 0 else 'N/A',
        'kel_temperature': int(((data['main']['temp']) - 273) * 9 / 5 + 32) if 'main' in data and 'temp' in data['main'] else 'N/A',
        'cel_temperature': int(data['main']['temp']) - 273 if 'main' in data and 'temp' in data['main'] else 'N/A',
        'pressure': data['main']['pressure'] if 'main' in data and 'pressure' in data['main'] else 'N/A',
        'humidity': data['main']['humidity'] if 'main' in data and 'humidity' in data['main'] else 'N/A',
        'wind': data['wind']['speed'] if 'wind' in data and 'speed' in data['wind'] else 'N/A',
        't': datetime.datetime.now()
    }    
     # city=request.POST.get('city','mohali')
    # if city is "":
    #     url=f'https://api.openweathermap.org/data/2.5/weather?q=mohali&appid=972e2c41d9666b571cff6f580122bf5d'
    # else:
    #     url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=972e2c41d9666b571cff6f580122bf5d'
    # payload={
    #     'name': data['name'],
    #     'weather':data['weather'][0]['main'],
    #     "description":data['weather'][0]['description'],
    #     'country':data['sys']['country'],
    #     'icon':data['weather'][0]['icon'],
    #     'kel_temperature':int(((data['main']['temp'])-273)*9/5+32),
    #     'cel_temperature':int(data['main']['temp'])-273,
    #     'pressure':data['main']['pressure'],
    #     'humidity':data['main']['humidity'],
    #     'wind':data['wind']['speed'],
    #     't':datetime.datetime.now()
    # }    
    context={'data':payload}    
    return render(request,'home.html',context)