import os
from dotenv import load_dotenv
from modules.download import get, download
from modules.set_filename import set_filename


def fetch_nasa_epic(api_key, path_download, prefix_filename):
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
    load_dotenv()
    NASA_KEY = os.getenv("NASA")
    fetch_nasa_epic(NASA_KEY, "Nasa_Epic", "epic")


if __name__ == "__main__":
    main()
