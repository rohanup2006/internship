import requests
def weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=b95e094a63afb276a942b0a9c32c3bb2&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(data['main']['temp'])
        print(data['main']['feels_like'])
        print(data['main']['temp_min'])
        print(data['main']['temp_max'])
        print(data['main']['pressure'])
        print(data['main']['humidity'])
        print(data['main']['sea_level'])
        print(data['main']['grnd_level'])
    except requests.exception.ReadTimeout as e:
         print(e)
city = input("enter the city name:")
weather_data(city)       