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

