import tkinter as tk
from PIL import ImageTk, Image
import requests
import random
import textwrap
import time


def print_nasa_explanation(data: dict):
    """
    Print interesting information about a daily nasa picture.

    :param data: a dictionary representing a parsed response from the NASA picture of the day API.
    :precondition: provide the function with an argument as defined by the PARAM statement above.
    :postcondition: print interesting information about the picture.
    """
    print(f'The image you see is titled: {data["title"]}.')
    print(f'It is the picture of the day from {data["date"]}!')
    print('Here is some cool information about that image!\n')
    formatted_text = textwrap.wrap(data["explanation"], width=100)
    for line in formatted_text:
        print(line)


def nasa_query() -> dict:
    """
    Get, parse, and return a date-randomized response from the NASA APOD API.

    :precondition: the NASA APOD API is fully functional. The API key remains valid.
    :postcondition: return an object as defined by the return statement below.
    :return: a dictionary representing a parsed response from the NASA picture of the day API.
    """
    # api query url assembly
    year = random.randint(1996, 2019)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    root = 'https://api.nasa.gov/planetary/apod?api_key='
    key = 'wtxdhlKb5seLp282a6Dsd3jofPYpcTdYiKupDaXC'
    config = f'&date={year}-{month}-{day}'
    url = root + key + config

    response = requests.get(url)
    return response.json()


def display_nasa_image(image):
    """
    Display an image in a tkinter window for 30 seconds, then close the window.

    :param image: a response object representing a streamed image file.
    :precondition: provide the function with an argument as defined by the PARAM statement above.
    :postcondition: open a tkinter window with an image in it for 30 seconds, then close that window.
    """
    tkinter_gui = tk.Tk()
    with Image.open(image.raw) as img:
        tk_img = ImageTk.PhotoImage(img)
    canvas = tk.Canvas(tkinter_gui, width=tk_img.width(), height=tk_img.height())
    canvas.create_image(0, 0, anchor='nw', image=tk_img)
    canvas.pack()
    # Close the tkinter window after 30 seconds.
    tkinter_gui.after(30000, lambda: tkinter_gui.destroy())
    tkinter_gui.mainloop()


def main():
    """
    Print information about and display a random picture of the day from NASA's APOD API every five minutes.
    """
    while True:
        nasa_response = nasa_query()
        print_nasa_explanation(nasa_response)
        nasa_image = requests.get(nasa_response['url'], stream=True)
        display_nasa_image(nasa_image)
        time.sleep(270)


if __name__ == "__main__":
    main()
