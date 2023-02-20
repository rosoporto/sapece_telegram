import os
import requests
from urllib.parse import urlencode


def get(value, params=None):
    if params:
        params = urlencode(params)
        r = requests.get(value, params=params)
    else:
        print("Else")
        r = requests.get(value)
    r.raise_for_status()
    return r


def download(url: str, dest_folder: str, filename=""):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    if not filename:
        filename = url.split("/")[-1].replace(" ", "_")  # be careful with file names
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print("saving to", os.path.abspath(file_path))
        with open(file_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))


if __name__ == '__main__':
    download("http://website.com/Motivation-Letter.docx", dest_folder="mydir")