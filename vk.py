import requests

VK_API_URL = "https://api.vk.com/method"
VK_API_VERSION = "5.131"


def get_upload_url(token, group_id):
    url = f"{VK_API_URL}/photos.getWallUploadServer"
    params = {
        "access_token": token,
        "v": VK_API_VERSION,
        "group_id": group_id,
    }

    response = requests.get(url=url, params=params)
    response.raise_for_status()
    response_object = response.json()

    upload_url = response_object["response"]["upload_url"]

    return upload_url


def upload_photo(token: str, upload_url: str, filename: str) -> dict:
    with open(filename, "rb") as file:
        params = {"access_token": token, "v": VK_API_VERSION}
        files = {"photo": file}

        response = requests.post(url=upload_url, params=params, files=files)
        response.raise_for_status()
        response_object = response.json()

    return response_object


def save_photo(token: str, upload_params: dict, group_id: int) -> tuple[int, int]:
    url = f"{VK_API_URL}/photos.saveWallPhoto"
    params = {
        "access_token": token,
        "v": VK_API_VERSION,
        "group_id": group_id,
        "photo": upload_params["photo"],
        "server": upload_params["server"],
        "hash": upload_params["hash"],
    }

    response = requests.post(url=url, params=params)
    response.raise_for_status()
    response_object = response.json()

    saved_file_metadata = response_object["response"][0]  # ["resonse"] length == 1
    photo_id = saved_file_metadata["id"]
    owner_id = saved_file_metadata["owner_id"]

    return photo_id, owner_id


def publish_wall_post(
    token: str, group_id: int, message: str, owner_id: str, photo_id: str
):
    url = f"{VK_API_URL}/wall.post"
    params = {
        "access_token": token,
        "v": VK_API_VERSION,
        "owner_id": -group_id,
        "from_group": 1,
        "message": message,
        "attachments": f"photo{owner_id}_{photo_id}",
    }

    response = requests.post(url=url, params=params)
    response.raise_for_status()
    response_object = response.json()

    post_id = response_object["response"]["post_id"]
    return post_id
