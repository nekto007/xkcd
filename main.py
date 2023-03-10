import os
import random
from dotenv import load_dotenv
from requests import HTTPError

import vk
import xkcd


def main():
    load_dotenv()
    token = os.getenv("ACCESS_TOKEN")
    group_id = int(os.getenv("GROUP_ID"))
    random_comics_id = random.randint(1, xkcd.get_last_id_comics())
    comics_data = xkcd.get_comics_data(random_comics_id)
    try:
        filename, title = xkcd.fetch_comics_image(comics_data)
        upload_server_url = vk.get_upload_url(token, group_id)
        upload_params = vk.upload_photo(token, upload_server_url, filename)
        photo_id, owner_id = vk.save_photo(token, upload_params, group_id)
        post_id = vk.publish_wall_post(token, group_id, title, owner_id, photo_id)
    except HTTPError as error:
        print(error)

    finally:
        os.remove(filename)


if __name__ == "__main__":
    main()
