import os
import telegram
from dotenv import load_dotenv
from modules.get_image import getImage


def get_chat_id(token):
    bot = telegram.Bot(token=token)
    about_bot = bot.get_updates()
    try:
        return about_bot[0]["message"]["chat"]["id"]
    except Exception:
        print("Set Start in you're Bot")


def send_photo_telegram(token, photo):
    bot = telegram.Bot(token)
    chat_id = get_chat_id(token)
    bot.send_photo(chat_id=chat_id, photo=open(photo, 'rb'))
    return "Complate!"


def main():
    load_dotenv()
    TELEGRAM_KEY = os.getenv("TELEGRAM")
    send_photo_telegram(TELEGRAM_KEY, "foto")


if __name__ == "__main__":
    main()