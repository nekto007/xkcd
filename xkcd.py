import requests


def get_last_id_comics() -> int:
    response = requests.get("https://xkcd.com/info.0.json")
    response.raise_for_status()

    return response.json()["num"]
