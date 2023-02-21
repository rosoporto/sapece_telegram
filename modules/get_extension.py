import os
from urllib.parse import urlparse


def get_extension(url):
    path_file = urlparse(url).path
    return os.path.splitext(path_file)[-1]


def main():
    """
    Функция возвращает расширение файла по ссылке
    """
    url = "https://example.com/txt/hello%20world.txt?v=9#python"
    print(get_extension(url))


if __name__ == "__main__":
    main()
