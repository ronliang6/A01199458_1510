import requests


def get_weather_data():
    api_key = "96bba64ba34672da132c1a987ad2fee6"
    lat = 49.24
    long = -123.15
    config = '&units=metric'
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&appid={api_key}{config}'
    print(url)

    api_return = requests.get(url)
    weather_json = api_return.json()

    print(weather_json['current'])


def main():
    get_weather_data()


if __name__ == "__main__":
    main()
