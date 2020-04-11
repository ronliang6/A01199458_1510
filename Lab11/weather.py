import requests
import time


def print_daily_summary(weather_data_day: dict):
    """
    Print a summary of the provided weather data.

    :param weather_data_day: a dictionary containing a day's weather information. Must be in the same format as the
    OpenWeatherAPI One Call JSON.
    :precondition: The location must be Vancouver, B.C., Canada.
    :postcondition: print the following weather information about the day: date and time, temperature low and high,
    sunrise and sunset time, relative humidity, wind speed, and weather type description.
    """
    date_time = time.localtime(weather_data_day['dt'])
    sunrise_time = time.localtime(weather_data_day['sunrise'])
    sunset_time = time.localtime(weather_data_day['sunset'])
    print(f"\nForecast for Vancouver on {date_time[2]}/{date_time[1]}/{date_time[0]}, at {date_time[3]}:00 local time.")
    print(f"Temperature low: {weather_data_day['temp']['min']}C. Temperature high: {weather_data_day['temp']['max']}C.")
    print(f"Time of sunrise is: {sunrise_time[3]}:{sunrise_time[4]:02} local time.", end=" ")
    print(f"Time of sunset is: {sunset_time[3]}:{sunset_time[4]:02} local time.")
    print(f"Humidity (rh) is {weather_data_day['humidity']}%.")
    print(f"Wind speed is {weather_data_day['wind_speed']}m/s.")
    print(f"The weather is expected to be {weather_data_day['weather'][0]['description']}.")


def print_weather_summary(weather_data: dict, days: int):
    """
    Print daily weather summaries for every day up including today until (and excluding) a given number of days.

    :param weather_data: a dictionary containing a day's weather information. Must be in the same format as the
    OpenWeatherAPI One Call JSON.
    :param days: an int in the range [1, x], where x is how many days of data are contained in weather_data.
    :precondition: provide the function with valid arguments according to the PARAM statements above.
    :postcondition: print daily weather summaries for a specified number of consecutive days starting from today.
    """
    for day in range(days):
        print_daily_summary(weather_data["daily"][day])


def get_weather_data() -> dict:
    """
    Query OpenWeather One Call API return the data parsed into a dictionary.

    The API call is configured to return metric values for Vancouver, B.C., Canada.

    :precondition: the API key must remain valid. The OpenWeather One Call API must be supported and functional.
    :postcondition: return an object as defined by the return PARAM below.
    :return: a dictionary representing various weather data, parsed from a JSON file response from the API Call.
    """
    # Creating the url for the api call
    api_key = "96bba64ba34672da132c1a987ad2fee6"
    lat = 49.24
    long = -123.15
    config = '&units=metric'
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&appid={api_key}{config}'

    # Querying and JSON parsing
    api_return = requests.get(url)
    weather_data = api_return.json()
    return weather_data


def main():
    """
    Run an application that prints daily weather data for today and a specified number of consecutive days.

    :precondition: The user enters an int as input.
    :postcondition: Print weather data for a number of days equal to the input if the 1 <= input <= 8,
    otherwise print a useful error message.
    """
    try:
        print("This weather app can only check days from today up to seven days in the future.")
        days_requested = int(input('Including today, how many days of weather would you like to view information for?'))
        if not 1 <= days_requested <= 8:
            raise ValueError("You must request a number of days in the range [1, 8].")
    except ValueError as error_message:
        print(error_message)
    else:
        weather_data = get_weather_data()
        print_weather_summary(weather_data, days_requested)


if __name__ == "__main__":
    main()
