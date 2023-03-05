import os
from dotenv import load_dotenv
from fetch_spacex_images import fetch_spacex_last_launch
from fetch_nasa_apod import fetch_urls_nasa_apod, fetch_nasa_apod
from fetch_nasa_epic import fetch_nasa_epic


def main():
    print(fetch_spacex_last_launch("foto", "space"))

    # load_dotenv()
    # NASA_KEY = os.getenv("NASA")

    # links_from_nasa= fetch_urls_nasa_apod(NASA_KEY)
    # fetch_nasa_apod(links_from_nasa, "Nasa_Apod", "apod")
    # fetch_nasa_epic(NASA_KEY, "Nasa_Epic", "epic")


if __name__ == "__main__":
    main()
