import requests

api_key = '56fb9d544db77bb860b7954a6fafea38'

user_input = input(' Enter city: ')
print(user_input)

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric")

if  weather_data.json()['cod'] == '404':
    print("No city Found")
else:    
    weather = weather_data.json()['weather'][0]['main']
    temp =   weather_data.json()['main']['temp']

print(f"The Weather in {user_input} is:{weather}")
print(f"The Temperature in {user_input}is:{temp}F")
