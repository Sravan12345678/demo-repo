import requests

City_Name ="Hyderabad"
API_key = "f5d0276e995057ede731cdf802f8ede8"
url =  f"https://api.openweathermap.org/data/2.5/weather?q={City_Name}&appid={API_key}&units=metric"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('Weather is',data['weather'][0])
    print('Current Temperature is',data['main']['temp'])
    print('Current Temperature Feels like is',data['main'])
    print('humidity is',data['main']['humidity'])
