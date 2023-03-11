import os
import random
from dotenv import load_dotenv
from requests import HTTPError

import vk
import xkcd


def main():
    load_dotenv()
    token = os.getenv("VK_ACCESS_TOKEN")
    group_id = int(os.getenv("VK_GROUP_ID"))
    random_comics_id = random.randint(1, xkcd.get_last_comics_id())
    get_comics_metadata = xkcd.get_comics_metadata(random_comics_id)
    try:
        title = get_comics_metadata['title']
        filename = xkcd.fetch_comics_image(get_comics_metadata['img'])
        upload_server_url = vk.get_upload_url(token, group_id)
        upload_params = vk.upload_photo(token, upload_server_url, filename)
        photo_id, owner_id = vk.save_photo(token, upload_params["photo"], upload_params["server"],
                                           upload_params["hash"], group_id)
        post_id = vk.publish_wall_post(token, group_id, title, owner_id, photo_id)
    except HTTPError as error:
        print(error)

    finally:
        os.remove(filename)


if __name__ == "__main__":
    main()
