import os
import requests
from dotenv import load_dotenv
from modules.download import get, download
from modules.set_filename import set_filename


def get_last_start(url):
    r = get(url)
    last_start =r.json()[-1]
    if len(last_start["links"]["flickr"]["original"]) > 0:
        return last_start
    else:
        r = get(url + "latest")
        return r.json()


def fetch_spacex_last_launch(foto_path, prefix, id="5eb87d47ffd86e000604b38a"):
    url = "https://api.spacexdata.com/v5/launches/" + id
    r = get(url).json()
    photos = r["links"]["flickr"]["original"]
    for index, photos in enumerate(photos):
        photo_name = prefix + str(index) + ".jpg"
        download(photos, foto_path, photo_name)
    else:
        return "Complate!"


def get_space_foto(api, count_image=3):
    params = {"count": count_image, "api_key": api}
    r = get("https://api.nasa.gov/planetary/apod", params=params)
    return [item["hdurl"] for item in r.json()]


def download_nasa_apod(links, path_foto, prefix_name_foto):
    for index, link in enumerate(links):
        file_name = set_filename(link, "nasa_apod", "_", str(index))
        download(link, "Nasa", file_name)
    else:
        print("Complate!")


def download_nasa_epic(api_key, path_download, prefix_filename):
    params = {"api_key": api_key}
    url = f"https://api.nasa.gov/EPIC/api/natural/all"
    all_date = get(url, params=params)
    last_date = all_date.json()[0]['date']
    url = f"https://api.nasa.gov/EPIC/api/natural/date/{last_date}"
    fotos_last_day = get(url, params=params)

    for index, snapshot_data in enumerate(fotos_last_day.json()):
        last_date = last_date.replace("-", "/")
        snapshot = f"https://api.nasa.gov/EPIC/archive/natural/{last_date}/png/{snapshot_data['image']}.png"
        file_name = set_filename(snapshot, prefix_filename, "_", str(index))

        download(snapshot, path_download, file_name, params)
    else:
        return "Complate!"



def main():
    #print(fetch_spacex_last_launch("foto", "space"))
    load_dotenv()
    NASA_KEY = os.getenv("NASA")
    # links_from_nasa= get_space_foto(NASA_KEY)
    # download_nasa_apod(links_from_nasa, "Nasa", "nasa_apod")

    download_nasa_epic(NASA_KEY, "Nasa_Epic", "epic")


if __name__ == "__main__":
    main()
