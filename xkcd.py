import os

import requests


def get_comics_data(comics_id):
    response = requests.get(f'https://xkcd.com/{comics_id}/info.0.json')
    response.raise_for_status()

    return response.json()


def fetch_comics_image(comics_data):
    title = comics_data['title']
    image_url = comics_data['img']
    filename = os.path.basename(image_url)

    response = requests.get(image_url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)
    return filename, title


def get_last_id_comics() -> int:
    response = requests.get("https://xkcd.com/info.0.json")
    response.raise_for_status()

    return response.json()["num"]
