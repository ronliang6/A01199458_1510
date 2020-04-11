import requests
import time


def print_daily_summary(weather_data_day: dict):
    date_time = time.localtime(weather_data_day['dt'])
    sunrise_time = time.localtime(weather_data_day['sunrise'])
    sunset_time = time.localtime(weather_data_day['sunset'])
    print(f"\nForecast for Vancouver on {date_time[2]}/{date_time[1]}/{date_time[0]}, at {date_time[3]}:00 local time.")
    print(f"Temperature low: {weather_data_day['temp']['min']}C. Temperature high: {weather_data_day['temp']['max']}C.")
    print(f"Time of sunrise is: {sunrise_time[3]}:{sunrise_time[4]} local time.", end="")
    print(f"Time of sunset is: {sunset_time[3]}:{sunset_time[4]} local time.")
    print(f"Humidity (rh) is {weather_data_day['humidity']}%.")
    print(f"Wind speed is {weather_data_day['wind_speed']}m/s.")
    print(f"The weather is expected to be {weather_data_day['weather'][0]['description']}.")


def print_weather_summary(weather_data: dict, days: int):
    for day in range(days):
        print_daily_summary(weather_data["daily"][day])


def get_weather_data() -> dict:
    # Creating the url for the api call
    api_key = "96bba64ba34672da132c1a987ad2fee6"
    lat = 49.24
    long = -123.15
    config = '&units=metric'
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&appid={api_key}{config}'

    # Querying and JSON parsing
    api_return = requests.get(url)
    weather_json = api_return.json()
    return weather_json


def main():
    weather_json = get_weather_data()
    try:
        print("This weather app can only check days from today up to seven days in the future.")
        days_requested = int(input('Including today, how many days of weather would you like to view information for?'))
        if not 1 <= days_requested <= 8:
            raise ValueError("You must request a number of days in the range [1, 8].")
        else:
            print_weather_summary(weather_json, days_requested)
    except ValueError as error_message:
        print(error_message)


if __name__ == "__main__":
    main()
