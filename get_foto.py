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


def main():
    foto_path = 'foto'
    prefix_foto_name = 'space'
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    r = get(url).json()
    photos = r["links"]["flickr"]["original"]
    for index, photos in enumerate(photos):
        photo_name = prefix_foto_name + str(index) + ".jpg"
        download(photos, foto_path, photo_name)




if __name__ == "__main__":
    main()