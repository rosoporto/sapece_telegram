from modules.get_extension import get_extension


def set_filename(link_to_file, *args):
        extension_file = get_extension(link_to_file)
        args += (extension_file,)
        return "".join(args)


def main():
    url = "https://apod.nasa.gov/apod/image/2004/PotatoPod_Sutton_5332.jpg"
    print(set_filename(url, "nasa_apod", "_", 0))


if __name__ == "__main__":
      main()