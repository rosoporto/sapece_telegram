import requests
from modules.download import download


def get(value, params=None):
    if not params:
        r = requests.get(value, params=params)
    else:
        r = requests.get(value)
    r.raise_for_status()
    return r


def get_last_start(url):
    r = get(url)
    last_start =r.json()[-1]
    if len(last_start["links"]["flickr"]["small"]) > 0:
        return last_start
    else:
        r = get(url + "latest")
        return r.json()


def main():
    # foto_path = 'foto'
    # foto_name = 'hubble.jpeg'
    # url_foto = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    # download(url_foto, dest_folder=foto_path)

    url = "https://api.spacexdata.com/v5/launches/"
    print(get_last_start(url))


if __name__ == "__main__":
    main()