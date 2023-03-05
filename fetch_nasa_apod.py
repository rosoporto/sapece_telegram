import os
from dotenv import load_dotenv
from modules.download import get, download
from modules.set_filename import set_filename


def fetch_urls_nasa_apod(api, count_image=3):
    params = {"count": count_image, "api_key": api}
    r = get("https://api.nasa.gov/planetary/apod", params=params)
    return [item["hdurl"] for item in r.json()]


def fetch_nasa_apod(links, path_foto, prefix_name_foto):
    for index, link in enumerate(links):
        file_name = set_filename(link, prefix_name_foto, "_", str(index))
        download(link, path_foto, file_name)
    else:
        print("Complate!")


def main():
    load_dotenv()
    NASA_KEY = os.getenv("NASA")
    links_from_nasa= fetch_urls_nasa_apod(NASA_KEY)
    fetch_nasa_apod(links_from_nasa, "Nasa_Apod", "apod")


if __name__ == "__main__":
    main()