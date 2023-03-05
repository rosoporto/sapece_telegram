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


def main():
    load_dotenv()
    TELEGRAM_KEY = os.getenv("TELEGRAM")
    foto = getImage("foto")[0]
    print(foto)
    bot = telegram.Bot(token=TELEGRAM_KEY)
    chat_id = get_chat_id(TELEGRAM_KEY)

    # #bot.send_message(chat_id=chat_id, text=f"You are chat id {chat_id}!")
    bot.send_document(chat_id=chat_id, document=open(foto, 'rb'))


if __name__ == "__main__":
    main()