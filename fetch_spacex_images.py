from modules.download import get, download


def fetch_spacex_last_launch(foto_path, prefix, id="5eb87d47ffd86e000604b38a"):
    url = "https://api.spacexdata.com/v5/launches/"
    r = get(url).json()[-1]
    if not r["links"]["flickr"]["original"]:
        url = "https://api.spacexdata.com/v5/launches/" + id
        r = get(url).json()
    photos = r["links"]["flickr"]["original"]
    for index, photos in enumerate(photos):
        photo_name = prefix + str(index) + ".jpg"
        download(photos, foto_path, photo_name)
    else:
        return "Complate!"


def main():
    print(fetch_spacex_last_launch("foto", "space"))


if __name__ == "__main__":
    main()