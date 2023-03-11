import os

import requests


def get_comics_metadata(comics_id):
    response = requests.get(f'https://xkcd.com/{comics_id}/info.0.json')
    response.raise_for_status()

    return response.json()


def fetch_comics_image(image_url):
    filename = os.path.basename(image_url)

    response = requests.get(image_url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)
    return filename


def get_last_comics_id() -> int:
    response = requests.get("https://xkcd.com/info.0.json")
    response.raise_for_status()

    return response.json()["num"]
