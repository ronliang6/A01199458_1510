import requests


def print_daily_summary(weather_data_day: dict):
    pass


def print_weather_summary(weather_data: dict, days: int):
    for day in range(days):
        print_daily_summary(weather_data["daily"][day])


def get_weather_data():
    # Creating the url for the api call
    api_key = "96bba64ba34672da132c1a987ad2fee6"
    lat = 49.24
    long = -123.15
    config = '&units=metric'
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&appid={api_key}{config}'

    api_return = requests.get(url)
    weather_json = api_return.json()
    return weather_json


def main():
    weather_json = get_weather_data()
    try:
        days_requested = int(input('Including today, how many days of weather would you like to view information for?'))
        if not 1 <= days_requested <= 8:
            raise ValueError("You must request a number of days in the range [1, 8].")
        else:
            print_weather_summary(weather_json, days_requested)
    except ValueError as error_message:
        print(error_message)


if __name__ == "__main__":
    main()
