from screenshot import save_images, delete_images
from upload import upload_images
import logging

logging.basicConfig(
    format='%(asctime)s %(module)s.%(funcName)s:%(levelname)s:%(message)s',
    datefmt='%m/%d/%Y %I_%M_%S %p',
    filename='log_file',
    level=logging.INFO
)

def main():
    url = "https://twitter.com/lavishsaluja/status/1314130099399061504"
    album_title = 'super-sonic'
    auth_file_name = None

    photo_list = save_images(url)
    # upload_images(photo_list, album_title, auth_file_name)
    # delete_images(photo_list)

if __name__ == "__main__":
    main()
