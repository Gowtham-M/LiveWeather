from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def get_html_content(city):
    import requests
    '''USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE'''
    city = city.replace(' ', '+')
    html_content = requests.get(f'https://www.google.com/search?q=weather+{city}').content
    return html_content

def hi(request):
    weather_data = None
    if 'city' in request.GET:
        city = request.GET.get('city')
        html_content = get_html_content(city)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        weather_data = dict()
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
        data = str.split('\n')
        weather_data['region'] = city.upper()
        weather_data['time'] = data[0]
        weather_data['sky'] = data[1]
        weather_data['temp'] = soup.find('div', attrs = {'class': 'BNeawe iBp4i AP7Wnd'}).text
    return render(request, 'DEMOAPP/hi.html', {'weather': weather_data})
