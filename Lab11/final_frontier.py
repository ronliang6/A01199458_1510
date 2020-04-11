import tkinter
import requests


def fun():
    config = '/search?q=moon'
    root = 'https://images-api.nasa.gov'
    url = root + config
    print(url)
    response = requests.get(url)
    data = response.json()
    print(data['collection']['items'][0]['data'][0])


def main():
    fun()


if __name__ == "__main__":
    main()