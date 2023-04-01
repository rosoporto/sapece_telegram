import os
import time
import random
import argparse
from dotenv import load_dotenv
from fetch_spacex_images import fetch_spacex_last_launch
from fetch_nasa_apod import fetch_urls_nasa_apod, fetch_nasa_apod
from fetch_nasa_epic import fetch_nasa_epic
from telegram_bot import send_photo_telegram
from modules.get_path_pictures import get_path_pictures


def main():
    parser = argparse.ArgumentParser(description='Скачивание фото по тематике фото и размещение их в Telegram-канале')
    parser.add_argument("images", help="Имя общей папки для всех картинок", default="images")
    parser.add_argument("pref_SX", help="Префикс имени картинок при сохранении с портала SpaceX", default="spaceX")
    parser.add_argument("pref_Apod", help="Префикс имени картинок при сохранении с портала NASA Apod", default="apod")
    parser.add_argument("pref_Epic", help="Префикс имени картинок при сохранении с портала NASA Epic", default="epic")
    parser.add_argument("time", help="Промежуток времени для публикации фото в Телеграм в часах", default=4)
    args = parser.parse_args()

    fetch_spacex_last_launch(args.images, args.pref_SX)

    load_dotenv()
    NASA_KEY = os.getenv("NASA")
    links_from_nasa= fetch_urls_nasa_apod(NASA_KEY)
    fetch_nasa_apod(links_from_nasa, args.images, args.pref_Apod)
    fetch_nasa_epic(NASA_KEY, args.images, args.pref_Epic)

    photos = get_path_pictures(args.images)
    TELEGRAM_KEY = os.getenv("TELEGRAM")
    pause = int(args.time) * 60


    while True:
        random.shuffle(photos)
        send_photo_telegram(TELEGRAM_KEY, photos[0])
        time.sleep(pause)


if __name__ == "__main__":
    main()