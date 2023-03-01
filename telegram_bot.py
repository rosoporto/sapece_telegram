import logging
import telegram


def get_chat_id(token):
    bot = telegram.Bot(token=token)
    about_bot = bot.get_updates()
    return about_bot[0]["message"]["chat"]["id"]

def main():
    import os
    from dotenv import load_dotenv
    load_dotenv()
    TELEGRAM_KEY = os.getenv("TELEGRAM")
    bot = telegram.Bot(token=TELEGRAM_KEY)
    chat_id = get_chat_id(TELEGRAM_KEY)
    bot.send_message(chat_id=chat_id, text=f"You are chat id {chat_id}!")




if __name__ == "__main__":
    main()