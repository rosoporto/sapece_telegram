import requests
from modules.download import get, download


def get_last_start(url):
    r = get(url)
    last_start =r.json()[-1]
    if len(last_start["links"]["flickr"]["original"]) > 0:
        return last_start
    else:
        r = get(url + "latest")
        return r.json()


def fetch_spacex_last_launch(foto_path="foto", prefix="space", id="5eb87d47ffd86e000604b38a"):
    url = "https://api.spacexdata.com/v5/launches/" + id
    r = get(url).json()
    photos = r["links"]["flickr"]["original"]
    for index, photos in enumerate(photos):
        photo_name = prefix + str(index) + ".jpg"
        download(photos, foto_path, photo_name)
    else:
        return "Complate!"


def main():
    print(fetch_spacex_last_launch())


if __name__ == "__main__":
    main()