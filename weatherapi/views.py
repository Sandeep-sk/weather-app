from django.shortcuts import render
import requests 
import datetime
def home(request):
    city=request.POST.get('city','mohali')
    if city is "":
        url=f'https://api.openweathermap.org/data/2.5/weather?q=mohali&appid=972e2c41d9666b571cff6f580122bf5d'
    else:
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=972e2c41d9666b571cff6f580122bf5d'
    data=requests.get(url).json()
    payload={
        'name': data['name'],
        'weather':data['weather'][0]['main'],
        "description":data['weather'][0]['description'],
        'country':data['sys']['country'],
        'icon':data['weather'][0]['icon'],
        'kel_temperature':int(((data['main']['temp'])-273)*9/5+32),
        'cel_temperature':int(data['main']['temp'])-273,
        'pressure':data['main']['pressure'],
        'humidity':data['main']['humidity'],
        'wind':data['wind']['speed'],
        't':datetime.datetime.now()
    }    
    context={'data':payload}
    return render(request,'home.html',context)