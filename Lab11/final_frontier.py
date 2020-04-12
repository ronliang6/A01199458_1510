import tkinter as tk
from PIL import ImageTk, Image
import requests
import random


def fun():
    # nasa api call for daily image with random date
    year = random.randint(1996, 2019)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    root = 'https://api.nasa.gov/planetary/apod?api_key='
    key = 'wtxdhlKb5seLp282a6Dsd3jofPYpcTdYiKupDaXC'
    config = f'&date={year}-{month}-{day}'
    url = root + key + config
    response = requests.get(url)
    data = response.json()

    # tkinter GUI
    top = tk.Tk()
    canvas = tk.Canvas(top, width=800, height=800)
    print(data['url'])

    response = requests.get(data['url'], stream=True)
    with Image.open(response.raw) as img:
        tk_img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor='nw', image=tk_img)
    canvas.pack()
    top.mainloop()


def main():
    fun()


if __name__ == "__main__":
    main()